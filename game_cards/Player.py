from DeckOfCards import DeckOfCards
from Card import Card
import random


class Player:
    """Represents a player in a card game."""

    def __init__(self, name, cards_amount=26):
        """Initialize the player with a name and a number of cards."""
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(cards_amount, int):
            raise ValueError("Cards amount must be a integer.")
        if not (10 <= cards_amount <= 26):
            cards_amount = 26
        self.name = name
        self.cards_amount = cards_amount
        self.deck = []

    def set_hand(self, deck_of_cards):
        """Set the player's hand with cards from a deck."""
        if not isinstance(deck_of_cards, DeckOfCards):
            raise ValueError("Expected a DeckOfCards instance.")
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
            raise ValueError("Expected a Card instance.")
        self.deck.append(card)
