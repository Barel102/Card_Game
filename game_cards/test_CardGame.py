from unittest import TestCase

from Player import Player
from CardGame import CardGame
from game_cards.Card import Card


class TestCardGame(TestCase):

    def setUp(self):
        self.player = Player("Barel")
        self.player2 = Player("Barel2")
        self.game = CardGame(self.player.name, self.player2.name, 26)

    def tearDown(self):
        del self.game
        del self.player
        del self.player2

    def test_cardgame_with_valid_inputs(self):
        self.assertEqual(self.game.player1.name, 'Barel')
        self.assertEqual(self.game.player2.name, 'Barel2')
        self.assertEqual(self.game.cards_amount, 26)

    def test_cardgame_with_invalid_inputs(self):
        with self.assertRaises(ValueError):
            CardGame(1, "barel2", 26)
        with self.assertRaises(ValueError):
            CardGame(1, 1, 26)
        with self.assertRaises(ValueError):
            CardGame("Barel", "barel2", "26")
        with self.assertRaises(ValueError):
            CardGame(None, "barel2", 26)
        with self.assertRaises(ValueError):
            CardGame("Barel", "barel2", None)

    def test_cardgame_with_default_cards_amount(self):
        temp_game = CardGame("Barel", "Barel2")
        self.assertEqual(temp_game.cards_amount, 26)

    def test_new_game_player_hands(self):
        self.assertEqual(len(self.game.player1.deck), 26)
        self.assertEqual(len(self.game.player2.deck), 26)
        self.assertEqual(len(self.game.deck.cards), 0)

        self.assertTrue(set(self.game.player1.deck).isdisjoint(set(self.game.player2.deck)))
        self.assertNotEqual(self.game.player1.deck[0], self.game.player2.deck[0])

    def test_new_game_cannot_be_called_twice(self):
        self.game.new_game()
        player1_deck_before = self.game.player1.deck.copy()
        player2_deck_before = self.game.player2.deck.copy()
        self.game.new_game()
        self.assertEqual(self.game.player1.deck, player1_deck_before)
        self.assertEqual(self.game.player2.deck, player2_deck_before)
        self.assertEqual(len(self.game.deck.cards), 0)

    def test_get_winner_returns_player1_when_they_have_more_cards(self):
        self.game.player1.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 8)]
        self.game.player2.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 6)]
        winner = self.game.get_winner()
        self.assertEqual(winner, self.game.player1)

    def test_get_winner_returns_player2_when_they_have_more_cards(self):
        self.game.player1.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 6)]
        self.game.player2.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 8)]
        winner = self.game.get_winner()
        self.assertEqual(winner, self.game.player2)

    def test_get_winner_returns_none_when_tie(self):
        self.game.player1.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 7)]
        self.game.player2.deck = [Card(value, suit) for suit in range(1, 5) for value in range(1, 7)]
        winner = self.game.get_winner()
        self.assertIsNone(winner)
