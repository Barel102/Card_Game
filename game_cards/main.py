from CardGame import CardGame

CARDS_AMOUNT = 26
GAME_ROUNDS = 10


def play_round(game):
    """Play a single round of the card game."""
    card1 = game.player1.get_card()
    card2 = game.player2.get_card()
    print(f'{game.player1.name} drew {card1}')
    print(f'{game.player2.name} drew {card2}')

    if card1 > card2:
        winner = game.player1
    else:
        winner = game.player2
    winner.add_card(card1)
    winner.add_card(card2)
    print(f'Round winner: {winner.name}\n')


def main():
    """Start and play the card game."""
    name1 = input('Please enter name for player1: ')
    name2 = input('Please enter name for player2: ')

    game = CardGame(name1, name2, CARDS_AMOUNT)

    print(f'\n{game.player1.name} has received cards: {[card.__str__() for card in game.player1.deck]}')
    print(f'{game.player2.name} has received cards: {[card.__str__() for card in game.player2.deck]}\n')

    for i in range(GAME_ROUNDS):
        print(f'[Round {i + 1}]')
        play_round(game)

    winner = game.get_winner()
    if winner is None:
        print('The game resulted in a tie!')
    else:
        print(f'The winner is: {winner.name}')


if __name__ == "__main__":
    main()
