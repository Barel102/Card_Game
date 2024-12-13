import random
from Card import Card

class DeckOfCards:
    def __init__(self):
        suits = range(1, 5)
        values = range(1, 14)
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def cards_shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card