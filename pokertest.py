import random
from card import Card
from deck import Deck

# Define the hand rankings
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

# Helper function to convert card values to numerical values
def evaluate_hand(hand):
    # Sort the hand by card values
    sorted_hand = sorted(hand, key=lambda card: Card.value_dict[card.value], reverse=True)
    values = [card.value for card in sorted_hand]
    suits = [card.suit for card in sorted_hand]
    
    # Check for flush
    if len(set(suits)) == 1:
        # Check for straight flush or royal flush
        if check_straight(values):
            if values == ['A', 'K', 'Q', 'J', '10']:
                return "Royal Flush", sorted_hand
            return "Straight Flush", sorted_hand
        
        return "Flush", sorted_hand

    # Check for straight
    if check_straight(values):
        return "Straight", sorted_hand

    # Count occurrences of each card value
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
    # Convert face cards to numerical values
    num_values = sorted([Card.value_dict[v] for v in values], reverse=True)
    # Check for 5 consecutive values
    for i in range(len(num_values) - 4):
        if num_values[i] - num_values[i + 4] == 4:
            return True
    return False

def compare_hands(hand1, hand2):
    rank_order = {rank: i for i, rank in enumerate(special_hands)}

    rank1, sorted_hand1 = evaluate_hand(hand1)
    rank2, sorted_hand2 = evaluate_hand(hand2)

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


def deal_hands(deck):
    return [deck.deal() for _ in range(2)], [deck.deal() for _ in range(2)]

def deal_community_cards(deck, count=5):
    return [deck.deal() for _ in range(count)]

def play_game():
    deck = Deck()
    
    # Deal hands to two players
    player1_hand, player2_hand = deal_hands(deck)
    print("Player 1 Hand:", player1_hand)
    print("Player 2 Hand:", player2_hand)
    
    
    community_cards = deal_community_cards(deck)
    
    print(f"Community Cards:, {community_cards[0]}, {community_cards[1]}, {community_cards[2]}")
    
    # Combine hands with community cards
    player1_combined = player1_hand + community_cards
    player2_combined = player2_hand + community_cards
    
    # Evaluate and compare hands
    result = compare_hands(player1_combined, player2_combined)
    if result > 0:
        print("Player 1 wins!")
    elif result < 0:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Play the game
if __name__ == "__main__":
    play_game() 