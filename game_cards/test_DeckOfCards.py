from unittest import TestCase
from DeckOfCards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self):
        """Set up a new deck of cards before each test."""
        self.deck = DeckOfCards()

    def tearDown(self):
        """Clean up the deck after each test."""
        del self.deck

    def test_deck_initialization(self):
        """Test that the deck contains 52 cards."""
        self.assertEqual(len(self.deck.cards), 52)

    def test_cards_shuffle(self):
        """Test that shuffling the deck randomizes the order."""
        copy_card_order = self.deck.cards.copy()
        self.deck.cards_shuffle()
        shuffled_order = self.deck.cards
        self.assertNotEqual(copy_card_order, shuffled_order)

    def test_deal_one(self):
        """Test that a card is removed from the deck after dealing."""
        dealt_card = self.deck.deal_one()
        self.assertNotIn(dealt_card, self.deck.cards)
        self.assertNotEqual(len(self.deck.cards), len(self.deck.cards) - 1)

    def test_deal_one_returns_card(self):
        """Test that dealing a card returns a valid Card object."""
        dealt_card = self.deck.deal_one()
        self.assertIsInstance(dealt_card, Card)
