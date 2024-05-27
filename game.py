import random
from card import Card
from deck import Deck
from player import Player
from configuration import configuration


class Game:
    special_hands = [
        "Royal Flush",
        "Straight Flush",
        "Four of a Kind",
        "Full House",
        "Flush",
        "Straight",
        "Three of a Kind",
        "Two Pair",
        "One Pair",
        "High Card"
    ]

    def __init__(self, players, starting_chips):
        self.deck = Deck()
        self.players = [Player(name, starting_chips, is_bot=(i == 1)) for i, name in enumerate(players)]
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        self.turn_index = 0

    def reset_game(self):
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        self.turn_index = 0
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
            return "Four of a Kind", sorted_hand

        if 3 in value_counts.values() and 2 in value_counts.values():
            return "Full House", sorted_hand

        if 3 in value_counts.values():
            return "Three of a Kind", sorted_hand

        if list(value_counts.values()).count(2) == 2:
            return "Two Pair", sorted_hand

        if 2 in value_counts.values():
            return "One Pair", sorted_hand

        return "High Card", sorted_hand

    def check_straight(values):
        num_values = sorted([Card.value_dict[v] for v in values])
        for i in range(len(num_values) - 4):
            if num_values[i + 4] - num_values[i] == 4:
                return True
        return False

    def compare_hands(self, hand1, hand2):
        rank_order = {rank: i for i, rank in enumerate(self.special_hands)}

        rank1, sorted_hand1 = Game.evaluate_hand(hand1)
        rank2, sorted_hand2 = Game.evaluate_hand(hand2)

        print(f"Player 1 Hand Type: {rank1}")
        print(f"Player 2 Hand Type: {rank2}")

        if rank1 != rank2:
            return 1 if rank_order[rank1] < rank_order[rank2] else -1

        for card1, card2 in zip(sorted_hand1, sorted_hand2):
            if Card.value_dict[card1.value] > Card.value_dict[card2.value]:
                return 1
            elif Card.value_dict[card1.value] < Card.value_dict[card2.value]:
                return -1

        return 0

    def deal_hands(self):
        for player in self.players:
            player.hand = [self.deck.deal() for _ in range(2)]

    def deal_community_cards(self, count=5):
        self.community_cards = [self.deck.deal() for _ in range(count)]

    def betting_round(self):
        active_players = [player for player in self.players if not player.folded]
        while True:
            current_player = active_players[self.turn_index]
            if current_player.is_bot:
                action = random.choice(['fold', 'call', 'raise'])
                print(f"{current_player.name} chooses to {action}.")
            else:
                action = input(f"{current_player.name}, your current chips: {current_player.chips}, pot: {self.pot}. Do you want to fold, call, or raise? ").strip().lower()

            if action == 'fold':
                current_player.folded = True
            elif action == 'call':
                call_amount = self.current_bet - current_player.current_bet
                current_player.bet(call_amount)
                self.pot += call_amount
            elif action == 'raise':
                if current_player.is_bot:
                    raise_amount = random.randint(1, current_player.chips)
                else:
                    raise_amount = int(input("Enter the amount to raise: "))
                current_player.bet(self.current_bet - current_player.current_bet + raise_amount)
                self.current_bet += raise_amount
                self.pot += self.current_bet - current_player.current_bet + raise_amount

            self.turn_index = (self.turn_index + 1) % len(active_players)

            if all(player.current_bet == self.current_bet or player.folded for player in active_players):
                break

    def play_game(self):
        self.reset_game()

        self.deal_hands()
        print("Dealing hands to players.")
        for player in self.players:
            print(f"{player.name}'s hand: {player.hand}")

        self.betting_round()

        self.deal_community_cards(3)
        print(f"Community cards: {self.community_cards[:3]}")
        self.betting_round()

        self.deal_community_cards(1)
        print(f"Community cards: {self.community_cards[:4]}")
        self.betting_round()

        self.deal_community_cards(1)
        print(f"Community cards: {self.community_cards}")
        self.betting_round()

        active_players = [player for player in self.players if not player.folded]
        hands = [player.hand + self.community_cards for player in active_players]

        if len(active_players) == 1:
            winner = active_players[0]
        else:
            best_hand_index = 0
            for i in range(1, len(hands)):
                if self.compare_hands(hands[best_hand_index], hands[i]) < 0:
                    best_hand_index = i
            winner = active_players[best_hand_index]

        print(f"The winner is {winner.name} with the hand {winner.hand + self.community_cards}!")
        winner.chips += self.pot

# Play the game
if __name__ == "__main__":
    name, bot_name, chips = configuration()
    player_names = [name, bot_name]
    game = Game(player_names, chips)
    game.play_game()
