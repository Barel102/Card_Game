from game_cards.Player import Player
from DeckOfCards import DeckOfCards


class CardGame:
    """Represents the card game logic."""

    def __init__(self, player1_name, player2_name, cards_amount=26):
        """Initialize the game with two players and a deck of cards."""
        if not isinstance(player1_name, str):
            raise ValueError("Player1 name must be a string.")
        if not isinstance(player2_name, str):
            raise ValueError("Player2 name must be a string.")
        if not isinstance(cards_amount, int):
            raise ValueError("cards_amount must be an integer.")
        if not (10 <= cards_amount <= 26):
            cards_amount = 26

        self.cards_amount = cards_amount
        self.player1 = Player(player1_name, cards_amount)
        self.player2 = Player(player2_name, cards_amount)
        self.deck = DeckOfCards()
        self.game_started = False
        self.new_game()

    def new_game(self):
        """Start a new game by shuffling the deck and dealing cards to players."""
        if self.game_started:
            print("Game already started")
            return

        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
        self.game_started = True

    def get_winner(self):
        """Determine the winner based on the number of cards left."""
        if len(self.player1.deck) > len(self.player2.deck):
            return self.player1
        elif len(self.player1.deck) < len(self.player2.deck):
            return self.player2
        return None