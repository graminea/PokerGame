class Player:
    def __init__(self, name, chips, is_bot=False):
        self.name = name
        self.chips = chips
        self.hand = []
        self.current_bet = 0
        self.folded = False
        self.is_bot = is_bot

    def bet(self, amount):
        if amount > self.chips:
            return False, f"Você não pode apostar {amount} fichas. Você só tem {self.chips} fichas."
        self.chips -= amount
        self.current_bet += amount
        return True, ""

    def reset_for_new_round(self):
        self.hand = []
        self.current_bet = 0
        self.folded = False

    def __repr__(self):
        return f"Player({self.name}, Chips: {self.chips}, Hand: {self.hand})"
