class Card:
    """
    Represents a playing card with a value and suit.
    """

    def __init__(self, value, suit):
        """Initialize a card with value and suit."""
        if not (isinstance(value, int) and isinstance(suit, int)):
            raise ValueError
        if not (value in range(1, 14) and suit in range(1, 5)):
            raise ValueError
        self.value = value
        self.suit = suit

    def __str__(self):
        """Return a string representation of the card."""
        if self.suit == 1:
            suit = "Diamonds"
        elif self.suit == 2:
            suit = "Spades"
        elif self.suit == 3:
            suit = "Hearts"
        else:
            suit = "Clubs"
        return f'{self.value} of {suit}'

    def __gt__(self, other):
        """Compare if this card is greater than another."""
        if not isinstance(other, Card):
            raise ValueError
        if self.value == other.value:
            return self.suit > other.suit

        return self.value > other.value

    def __eq__(self, other):
        """Check if this card is equal to another."""
        if not isinstance(other, Card):
            raise ValueError
        return self.value == other.value and self.suit == other.suit

    def __hash__(self):
        """Return a hash value based on card's value and suit."""
        return hash((self.value, self.suit))  # Combine value and suit for hashing