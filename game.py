import random
from card import Card
from deck import Deck
from player import Player
from colorama import Fore, Style, init
from countdown import countdown

init(autoreset=True)

class Game:
    special_hands = [
        "Royal Flush",
        "Straight Flush",
        "Quadra",
        "Full House",
        "Flush",
        "Straight",
        "Trinca",
        "Dois Pares",
        "Um Par",
        "Carta Alta"
    ]

    def __init__(self, players, starting_chips):
        self.deck = Deck()
        self.players = [Player(name, starting_chips, is_bot=(i == 1)) for i, name in enumerate(players)]
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        self.counter_round = 0

    def reset_game(self):
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        
        self.counter_round = 0
        for player in self.players:
            player.reset_for_new_round()

    def evaluate_hand(hand):
        sorted_hand = sorted(hand, key=lambda card: Card.value_dict[card.value], reverse=True)
        values = [card.value for card in sorted_hand]
        suits = [card.suit for card in sorted_hand]

        if len(set(suits)) == 1:
            if Game.check_straight(values):
                if values == ['A', 'K', 'Q', 'J', '10']:
                    return "Royal Flush", sorted_hand
                return "Straight Flush", sorted_hand
            return "Flush", sorted_hand

        if Game.check_straight(values):
            return "Straight", sorted_hand

        value_counts = {value: values.count(value) for value in values}

        if 4 in value_counts.values():
            return "Quadra", sorted_hand

        if 3 in value_counts.values() and 2 in value_counts.values():
            return "Full House", sorted_hand

        if 3 in value_counts.values():
            return "Trinca", sorted_hand

        if list(value_counts.values()).count(2) == 2:
            return "Dois Pares", sorted_hand

        if 2 in value_counts.values():
            return "Um Par", sorted_hand

        return "Carta Alta", sorted_hand

    @staticmethod
    def check_straight(values):
        num_values = sorted(set([Card.value_dict[v] for v in values]))
        for i in range(len(num_values) - 4):
            if num_values[i + 4] - num_values[i] == 4:
                return True
        return False

    def compare_hands(self, hand1, hand2):
        rank_order = {rank: i for i, rank in enumerate(self.special_hands)}

        rank1, sorted_hand1 = Game.evaluate_hand(hand1)
        rank2, sorted_hand2 = Game.evaluate_hand(hand2)

        return rank1, rank2, sorted_hand1, sorted_hand2

    def deal_hands(self):
        for player in self.players:
            player.hand = [self.deck.deal() for _ in range(2)]

    def deal_community_cards(self, count):
        new_cards = [self.deck.deal() for _ in range(count)]
        self.community_cards.extend(new_cards)
        return new_cards

    def betting_round(self, first_round, final_round=False):
        active_players = [player for player in self.players if not player.folded]
        while True:
            new_active_players = []
            for current_player in active_players:
                if current_player.folded:
                    continue  # Skip folded players

                print(f"\n{Fore.LIGHTBLACK_EX}Aposta atual: {self.current_bet}\n")  # Show the current bet
                self.counter_round += 0.5

                if current_player.is_bot:
                    action = random.choice(['fold', 'call', 'aumentar', 'all-in'] if final_round else ['fold','call', 'aumentar'])
                    print(f"{Fore.YELLOW}{current_player.name} escolheu {action}.\n")
                else:
                    if first_round:
                        print(f"\n{Fore.LIGHTBLACK_EX}{current_player.name}, suas fichas atuais: {current_player.chips}, pote: {self.pot}.\n")
                        countdown(3)
                        while True:
                            print(f"{Fore.MAGENTA}Escolha uma ação:\n1-Aumentar\n")
                            action = input(f"{Fore.GREEN}Ação: ").strip()
                            if action == '1':
                                action = 'aumentar'
                                break
                            else:
                                print(f"{Fore.RED}Opção inválida. Por favor, escolha 1 para aumentar.\n")
                    else:
                        while True:
                            print(f"{Fore.CYAN}{current_player.name}, suas fichas atuais: {current_player.chips}, pote: {self.pot}.\n")
                            print(f'Sua mão:{current_player.hand}')
                            countdown(3)
                            print(f"{Fore.MAGENTA}Escolha uma ação:\n1-Aumentar\n2-Mesa\n3-Fold\n" + ("4-All-IN\n" if final_round else ""))
                            action = input(f"{Fore.GREEN}Ação: ").strip()
                            if action == '1':
                                action = 'aumentar'
                                break
                            elif action == '2':
                                action = 'call'
                                break
                            elif action == '3':
                                action = 'fold'
                                break
                            elif action == '4' and final_round:
                                action = 'all-in'
                                break
                            else:
                                print(f"{Fore.RED}Opção inválida. Por favor, escolha 1, 2, 3" + (" ou 4\n" if final_round else "\n"))
                                continue

                if action == 'fold':
                    current_player.folded = True
                elif action == 'call':
                    call_amount = self.current_bet - current_player.current_bet
                    if call_amount > current_player.chips:
                        call_amount = current_player.chips
                    current_player.bet(call_amount)
                    self.pot += call_amount
                elif action == 'aumentar':
                    if current_player.is_bot:
                        raise_amount = random.randint(1, current_player.chips)
                    else:
                        while True:
                            try:
                                raise_amount = int(input(f"{Fore.GREEN}{Style.BRIGHT}Digite o valor para aumentar: \n"))
                                if raise_amount > current_player.chips:
                                    print(f"{Fore.RED}Você não pode aumentar mais fichas do que possui.\n")
                                else:
                                    break
                            except ValueError:
                                print(f"{Fore.RED}Entrada inválida. Por favor, digite um número inteiro válido.\n")

                    raise_amount = min(raise_amount, current_player.chips)
                    total_raise_amount = self.current_bet + raise_amount - current_player.current_bet
                    success, message = current_player.bet(total_raise_amount)
                    if not success:
                        print(f"{Fore.RED}{message}\n")
                        continue  # Prompt again
                    self.current_bet += raise_amount
                    self.pot += total_raise_amount
                    print(f'{current_player.name} aumentou {raise_amount} fichas')
                elif action == 'all-in':
                    all_in_amount = current_player.chips
                    current_player.bet(all_in_amount)
                    self.pot += all_in_amount
                    print(f"{Fore.RED}{current_player.name} foi All-IN com {all_in_amount} fichas!\n{Fore.RESET}")

                if not current_player.folded:
                    new_active_players.append(current_player)

                if self.counter_round == 1:
                    print(f"{Fore.LIGHTRED_EX}\nCartas comunitárias (Flop): {self.community_cards[:3]}\n")
                elif self.counter_round == 2:
                    print(f"{Fore.LIGHTRED_EX}\nCartas comunitárias (Turn): {self.community_cards[:4]}\n")
                elif self.counter_round == 3:
                    print(f"{Fore.LIGHTRED_EX}\nCartas comunitárias (River): {self.community_cards[:5]}\n")

                if final_round:
                    break  # Exit the loop if it's the final round

            if len(new_active_players) == 1 or final_round:  # If only one player remains, end the round
                break

            if all(player.current_bet == self.current_bet or player.folded for player in new_active_players):
                break

            active_players = new_active_players
            first_round = False  # After the first round, set the flag to False

            if self.counter_round == 3 and not final_round:
                final_round = True
                break  # Exit the loop to handle the final round outside



    def play_game(self):
        while True:  # Loop until a player runs out of chips
            self.reset_game()

            self.deal_hands()
            self.deal_community_cards(5)
            print(f"{Fore.MAGENTA}\nDistribuindo mãos para os jogadores.")
           
            print(f"{Fore.CYAN}Sua mão:{self.players[0].name}: {self.players[0].hand}")

            # Main game loop
            while True:
                final_round = self.counter_round == 3
                first_round = self.counter_round == 0
                self.betting_round(first_round=first_round, final_round=final_round)

                active_players = [player for player in self.players if not player.folded]
                if len(active_players) <= 1 or final_round:
                    break

            # Determine the winner of the round and award the pot
            if len(active_players) == 1:
                winner = active_players[0]
                print(f"{Fore.GREEN}O vencedor é {winner.name}!\n")
            else:
                hands = [player.hand + self.community_cards for player in active_players]
                hand_evaluations = [self.compare_hands(hands[i], hands[0]) for i in range(len(hands))]
                best_hand_index = max(range(len(hands)), key=lambda i: hand_evaluations[i][0])
                winner = active_players[best_hand_index]

                # Print the hand types correctly for each player
                for i, player in enumerate(active_players):
                    rank, _, _, _ = hand_evaluations[i]
                    print(f"{Fore.WHITE}{Style.BRIGHT}Tipo da mão de {player.name}: {rank}")
                    
                print(f"{Fore.YELLOW}O vencedor é {winner.name} com a mão {winner.hand + self.community_cards}!\n")

            winner.chips += self.pot

            # Check if any player has run out of chips
            if any(player.chips <= 0 for player in self.players):
                break

        print(f"{Fore.YELLOW}Fim do jogo! {winner.name} venceu o jogo com {winner.chips} fichas!")

