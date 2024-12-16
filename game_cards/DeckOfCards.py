import random
from Card import Card


class DeckOfCards:
    """Represents a deck of 52 playing cards."""

    def __init__(self):
        """Initialize the deck with all 52 cards."""
        self.cards = [Card(value, suit) for suit in range(1, 5)
                      for value in range(1, 14)]

    def cards_shuffle(self):
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)

    def deal_one(self):
        """Deal one card randomly from the deck."""
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
