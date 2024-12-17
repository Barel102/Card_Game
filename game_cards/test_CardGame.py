from unittest import TestCase

from Player import Player
from CardGame import CardGame
from game_cards.Card import Card


class TestCardGame(TestCase):
    def setUp(self):
        """Set up the testing environment before each test case."""
        self.player = Player("Barel", 26)
        self.player2 = Player("Barel2", 26)
        self.game = CardGame(self.player.name, self.player2.name, 26)

    def tearDown(self):
        """Clean up the testing environment after each test case."""
        del self.game
        del self.player
        del self.player2

    def test_valid_initialization(self):
        """Test that CardGame initializes correctly with valid inputs."""
        self.assertEqual(self.game.player1.name, 'Barel')
        self.assertEqual(self.game.player2.name, 'Barel2')
        self.assertEqual(self.game.cards_amount, 26)

    def test_invalid_player1_name(self):
        """Test that ValueError is raised if player1 name is invalid."""
        with self.assertRaises(ValueError):
            CardGame(1, "Barel2", 26)

    def test_invalid_player2_name(self):
        """Test that ValueError is raised if player2 name is invalid."""
        with self.assertRaises(ValueError):
            CardGame("Barel", 1, 26)

    def test_invalid_cards_amount_string(self):
        """Test that ValueError is raised if cards_amount is string."""
        with self.assertRaises(ValueError):
            CardGame("Barel", "Barel2", "26")

    def test_default_cards_amount_nine(self):
        """Test that cards_amount defaults to 26 if not provided."""
        temp_game = CardGame("Barel", "Barel2", 9)
        self.assertEqual(temp_game.cards_amount, 26)

    def test_default_cards_amount_twentySeven(self):
        """Test that cards_amount defaults to 26 if not provided."""
        temp_game = CardGame("Barel", "Barel2", 27)
        self.assertEqual(temp_game.cards_amount, 26)

    def test_new_game_player_hands_initialized(self):
        """Test that player hands are properly initialized in a new game."""
        self.assertEqual(len(self.game.player1.deck), 26)
        self.assertEqual(len(self.game.player2.deck), 26)
        self.assertEqual(len(self.game.deck.cards), 0)
        self.assertNotEqual(self.game.player1.deck[0], self.game.player2.deck[0])

    def test_new_game_cannot_be_called_twice(self):
        """Test that new_game does not reinitialize decks if called twice."""
        self.game.new_game()
        player1_deck_before = self.game.player1.deck.copy()
        player2_deck_before = self.game.player2.deck.copy()

        self.game.new_game()  # Attempt to call new_game again
        self.assertEqual(self.game.player1.deck, player1_deck_before)
        self.assertEqual(self.game.player2.deck, player2_deck_before)
        self.assertEqual(len(self.game.deck.cards), 0)

    def test_get_winner_player1_has_more_cards(self):
        """Test get_winner returns player1 when they have more cards."""
        self.game.player1.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 8)]
        self.game.player2.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 6)]
        winner = self.game.get_winner()
        self.assertEqual(winner, self.game.player1)

    def test_get_winner_player2_has_more_cards(self):
        """Test get_winner returns player2 when they have more cards."""
        self.game.player1.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 6)]
        self.game.player2.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 8)]
        winner = self.game.get_winner()
        self.assertEqual(winner, self.game.player2)

    def test_get_winner_returns_none_on_tie(self):
        """Test get_winner returns None when both players have equal cards."""
        self.game.player1.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 7)]
        self.game.player2.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 7)]
        winner = self.game.get_winner()
        self.assertIsNone(winner)
