from DeckOfCards import DeckOfCards
from Card import Card
import random


class Player:
    """Represents a player in a card game."""

    def __init__(self, name, cards_amount=26):
        """Initialize the player with a name and a number of cards."""
        if not (isinstance(name, str) and isinstance(cards_amount, int)):
            raise ValueError
        if not 10 <= cards_amount <= 26:
            cards_amount = 26
        self.cards_amount = cards_amount
        self.name = name
        self.deck = list()

    def set_hand(self, deck_of_cards):
        """Set the player's hand with cards from a deck."""
        if not isinstance(deck_of_cards, DeckOfCards):
            raise ValueError
        self.deck = [deck_of_cards.deal_one() for _ in range(self.cards_amount)]

    def get_card(self):
        """Get a random card from the player's hand."""
        if not len(self.deck) > 0:
            raise IndexError
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def add_card(self, card):
        """Add a card to the player's hand."""
        if not isinstance(card, Card):
            raise ValueError
        self.deck.append(card)
