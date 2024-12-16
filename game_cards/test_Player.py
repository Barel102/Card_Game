from unittest import TestCase
from unittest.mock import patch
from Card import Card
from Player import Player
from DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    """Unit tests for the Player class."""

    def setUp(self):
        """Set up the Player instance before each test."""
        self.player = Player("Barel")

    def tearDown(self):
        """Clean up the Player instance after each test."""
        del self.player

    def test_player_valid_input(self):
        """Test that Player initializes correctly with valid inputs."""
        self.assertEqual(self.player.name, "Barel")
        self.assertEqual(self.player.cards_amount, 26)

    def test_player_invalid_input(self):
        """Test that Player raises ValueError for invalid inputs."""
        with self.assertRaises(ValueError):
            Player(1)

        with self.assertRaises(ValueError):
            Player(None)

        with self.assertRaises(ValueError):
            Player("Barel", "26")

        with self.assertRaises(ValueError):
            Player("Barel", None)

    def test_default_cards_amount(self):
        """Test that Player defaults to 26 cards if cards_amount is invalid."""
        player = Player("Barel", 27)
        player2 = Player("Barel2", 9)
        self.assertEqual(player.cards_amount, 26)
        self.assertEqual(player2.cards_amount, 26)

    def test_set_hand_valid_deck(self):
        """Test that Player's set_hand works correctly with a valid deck."""
        with patch(
                'DeckOfCards.DeckOfCards.deal_one',
                side_effect=[Card(value, suit) for suit in range(1, 5) for value in range(1, 14)]
        ) as mock_deal_one:
            self.player.set_hand(DeckOfCards())
            self.assertEqual(len(self.player.deck), 26)
            self.assertEqual(mock_deal_one.call_count, 26)

            # Verify that expected cards are in the player's deck
            expected_cards = [Card(value, suit) for suit in range(1, 5) for value in range(1, 14)][:26]
            for card in expected_cards:
                self.assertIn(card, self.player.deck)

    def test_set_hand_invalid_deck(self):
        """Test that Player's set_hand raises ValueError for invalid decks."""
        with self.assertRaises(ValueError):
            self.player.set_hand("InvalidDeck")

        with self.assertRaises(ValueError):
            self.player.set_hand(None)

        with self.assertRaises(ValueError):
            self.player.set_hand(1)

        with self.assertRaises(ValueError):
            self.player.set_hand(list[1:2, 3:4])

    def test_get_card_valid(self):
        """Test that Player's get_card retrieves a card and removes it from the deck."""
        self.player.set_hand(DeckOfCards())
        card = self.player.get_card()
        self.assertIsInstance(card, Card)
        self.assertNotIn(card, self.player.deck)

    def test_get_card_empty_deck(self):
        """Test that Player's get_card raises IndexError when the deck is empty."""
        self.player.deck = []
        with self.assertRaises(IndexError):
            self.player.get_card()

    def test_add_card_valid(self):
        """Test that Player's add_card adds a valid card to the deck."""
        card = Card(1, 1)
        self.player.add_card(card)
        self.assertIn(card, self.player.deck)
        self.assertEqual(len(self.player.deck), 1)

    def test_add_card_invalid(self):
        """Test that Player's add_card raises ValueError for invalid cards."""
        with self.assertRaises(ValueError):
            self.player.add_card(Card(0, 1))

        with self.assertRaises(ValueError):
            self.player.add_card(Card(1, 0))

        with self.assertRaises(ValueError):
            self.player.add_card(Card("5", 1))

        with self.assertRaises(ValueError):
            self.player.add_card(Card(1, "5"))

        with self.assertRaises(ValueError):
            self.player.add_card(Card(None, 1))

        with self.assertRaises(ValueError):
            self.player.add_card(Card(1, None))