from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        """Set up test cards."""
        self.card1 = Card(10, 2)
        self.card2 = Card(5, 3)

    def tearDown(self):
        """Clean up test cards."""
        del self.card1
        del self.card2

    def test_init_valid_input(self):
        """Test initialization with valid inputs."""
        self.assertEqual(self.card1.value, 10)
        self.assertEqual(self.card1.suit, 2)

    def test_init_invalid_value_zero(self):
        """Test initialization with value 0."""
        with self.assertRaises(ValueError):
            Card(0, 1)

    def test_init_invalid_value_out_of_range(self):
        """Test initialization with value 14."""
        with self.assertRaises(ValueError):
            Card(14, 1)

    def test_init_invalid_value_string(self):
        """Test initialization with value as string."""
        with self.assertRaises(ValueError):
            Card("HI", 1)

    def test_init_invalid_value_none(self):
        """Test initialization with value as None."""
        with self.assertRaises(ValueError):
            Card(None, 1)

    def test_init_invalid_suit_zero(self):
        """Test initialization with suit 0."""
        with self.assertRaises(ValueError):
            Card(1, 0)

    def test_init_invalid_suit_out_of_range(self):
        """Test initialization with suit 5."""
        with self.assertRaises(ValueError):
            Card(1, 5)

    def test_init_invalid_suit_string(self):
        """Test initialization with suit as string."""
        with self.assertRaises(ValueError):
            Card(1, "HI")

    def test_init_invalid_suit_none(self):
        """Test initialization with suit as None."""
        with self.assertRaises(ValueError):
            Card(1, None)

    def test_card_min_value(self):
        """Test that the card with minimum value is created correctly."""
        card_min_value_suit = Card(1, 1)
        self.assertEqual(card_min_value_suit.value, 1)

    def test_card_min_suit(self):
        """Test that the card with minimum suit is created correctly."""
        card_min_value_suit = Card(1, 1)
        self.assertEqual(card_min_value_suit.suit, 1)

    def test_card_max_value(self):
        """Test that the card with maximum value is created correctly."""
        card_max_value_suit = Card(13, 4)
        self.assertEqual(card_max_value_suit.value, 13)

    def test_card_max_suit(self):
        """Test that the card with maximum suit is created correctly."""
        card_max_value_suit = Card(13, 4)
        self.assertEqual(card_max_value_suit.suit, 4)

    def test_gt_with_greater_value_true(self):
        """Test > operator returns True when the left card has a greater value."""
        self.assertTrue(self.card1 > self.card2)

    def test_gt_with_greater_value_false(self):
        """Test > operator returns False when the right card has a greater value."""
        self.assertFalse(self.card2 > self.card1)

    def test_gt_with_equal_value_different_suit_true(self):
        """Test > operator returns True when cards have equal values, but left card has a higher suit."""
        self.assertTrue(Card(10, 3) > self.card1)

    def test_gt_with_equal_value_different_suit_false(self):
        """Test > operator returns False when cards have equal values, but right card has a higher suit."""
        self.assertFalse(self.card1 > Card(10, 3))

    def test_gt_invalid_comparison_string(self):
        """Test > operator with invalid comparison to string."""
        with self.assertRaises(ValueError):
            self.card1 > 'hi'


    def test_eq_with_equal_cards(self):
        """Test == operator with equal cards."""
        self.assertTrue(self.card1 == Card(10, 2))

    def test_eq_with_different_cards(self):
        """Test == operator with different cards."""
        self.assertFalse(self.card1 == self.card2)

    def test_eq_invalid_comparison_string(self):
        """Test == operator with invalid comparison to string."""
        with self.assertRaises(ValueError):
            self.card1 == "Hi"