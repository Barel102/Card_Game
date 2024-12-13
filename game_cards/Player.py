from DeckOfCards import DeckOfCards
from Card import Card
import random

class Player:
    def __init__(self, name, cards_amount=26):
        if not (isinstance(name, str) and isinstance(cards_amount, int)):
            raise ValueError
        if not 10 <= cards_amount <= 26:
            cards_amount = 26
        self.cards_amount = cards_amount
        self.name = name
        self.deck = list()

    def set_hand(self, deck_of_cards):
        if not isinstance(deck_of_cards, DeckOfCards):
            raise ValueError
        self.deck = [deck_of_cards.deal_one() for _ in range(self.cards_amount)]

    def get_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def add_card(self, card):
        if not isinstance(card, Card):
            raise ValueError
        self.deck.append(card)