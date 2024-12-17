class Card:
    """Represents a playing card with a value (1-13) and suit (1-4)."""

    def __init__(self, value, suit):
        """Initialize a card with value (1-13) and suit (1-4)."""
        if not (isinstance(value, int) and isinstance(suit, int)):
            raise ValueError("Card value and suit must both be integers.")
        if not (1 <= value <= 13 and 1 <= suit <= 4):
            raise ValueError("Card value must be between 1-13, and suit must be between 1-4.")
        self.value = value
        self.suit = suit

    def __str__(self):
        """Return a string representation of the card."""
        suits = {1: "Diamonds", 2: "Spades", 3: "Hearts", 4: "Clubs"}
        return f'{self.value} of {suits[self.suit]}'

    def __gt__(self, other):
        """Compare if this card is greater than another card."""
        if not isinstance(other, Card):
            raise ValueError("Cannot compare a Card with a non-Card object.")
        if self.value == other.value:
            return self.suit > other.suit
        return self.value > other.value

    def __eq__(self, other):
        """Check if this card is equal to another card."""
        if not isinstance(other, Card):
            raise ValueError("Cannot compare a Card with a non-Card object.")
        return self.value == other.value and self.suit == other.suit

    def __hash__(self):
        """Override hash method to use the card's value and suit."""
        return hash((self.value, self.suit))