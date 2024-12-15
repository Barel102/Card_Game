from game_cards.Player import Player
from DeckOfCards import DeckOfCards


class CardGame:
    def __init__(self, player1_name, player2_name, cards_amount=26):
        if not (isinstance(player1_name, str) and isinstance(player2_name, str) and isinstance(cards_amount, int)):
            raise ValueError

        if not 10 <= cards_amount <= 26:
            cards_amount = 26

        self.cards_amount = cards_amount
        self.player1 = Player(player1_name, cards_amount)
        self.player2 = Player(player2_name, cards_amount)
        self.deck = DeckOfCards()
        self.game_started = False
        self.new_game()

    def new_game(self):
        if self.game_started:
            print('Game already started')
            return

        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
        self.game_started = True

    def get_winner(self):
        if len(self.player1.deck) > len(self.player2.deck):
            return self.player1
        elif len(self.player1.deck) < len(self.player2.deck):
            return self.player2
        return None
