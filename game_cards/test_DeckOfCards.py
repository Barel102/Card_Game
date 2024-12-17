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

    def test_deck_initialization_unique_cards(self):
        """Test that all cards in the deck are unique."""
        unique_cards = set(self.deck.cards)
        self.assertEqual(len(unique_cards), 52)

    def test_cards_shuffle_randomizes_order(self):
        """Test that shuffling the deck randomizes the order of cards."""
        original_order = self.deck.cards.copy()
        self.deck.cards_shuffle()
        shuffled_order = self.deck.cards
        self.assertNotEqual(original_order, shuffled_order)
        self.assertEqual(len(shuffled_order), 52)

    def test_shuffle_empty_deck(self):
        empty_deck = DeckOfCards()
        empty_deck.cards = []
        empty_deck.cards_shuffle()

    def test_deal_one(self):
        """Test that a card is removed from the deck after dealing."""
        initial_deck_length = len(self.deck.cards)
        dealt_card = self.deck.deal_one()
        self.assertIsNotNone(dealt_card)
        self.assertEqual(len(self.deck.cards), initial_deck_length - 1)
        self.assertNotIn(dealt_card, self.deck.cards)

    def test_deal_one_returns_valid_card(self):
        """Test that dealing a card returns a valid Card object."""
        dealt_card = self.deck.deal_one()
        self.assertIsInstance(dealt_card, Card)

    def test_deal_one_returns_none_if_deck_empty(self):
        temp_deck = DeckOfCards()
        temp_deck.cards = []
        self.assertIsNone(temp_deck.deal_one())