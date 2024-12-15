from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        """Set up test cards."""
        self.card1 = Card(10, 1)
        self.card2 = Card(5, 2)
        self.card3 = Card(10, 3)
        self.card4 = Card(10, 1)

    def tearDown(self):
        """Clean up test cards."""
        del self.card1
        del self.card2
        del self.card3

    def test_init_valid_input(self):
        """Test initialization with valid inputs."""
        self.assertEqual(self.card1.value, 10)
        self.assertEqual(self.card1.suit, 1)

    def test_init_invalid_value(self):
        """Test initialization with invalid values."""
        with self.assertRaises(ValueError):
            Card(0, 1)
        with self.assertRaises(ValueError):
            Card(14, 1)
        with self.assertRaises(ValueError):
            Card("HI", 1)
        with self.assertRaises(ValueError):
            Card(None, 1)

    def test_init_invalid_suit(self):
        """Test initialization with invalid suits."""
        with self.assertRaises(ValueError):
            Card(1, 0)
        with self.assertRaises(ValueError):
            Card(1, 5)
        with self.assertRaises(ValueError):
            Card(1, "HI")
        with self.assertRaises(ValueError):
            Card(1, None)

    def test_gt_with_greater_value(self):
        """Test > operator with different values."""
        self.assertTrue(self.card1 > self.card2)
        self.assertFalse(self.card2 > self.card1)

    def test_gt_with_equal_value_different_suit(self):
        """Test > operator with equal values but different suits."""
        self.assertTrue(self.card3 > self.card1)
        self.assertFalse(self.card1 > self.card3)

    def test_gt_invalid_other(self):
        """Test > operator with invalid types."""
        with self.assertRaises(ValueError):
            self.card1 > 'hi'
        with self.assertRaises(ValueError):
            self.card1 > 1
        with self.assertRaises(ValueError):
            self.card1 > None

    def test_eq_with_equal_cards(self):
        """Test == operator with equal cards."""
        self.assertTrue(self.card1 == self.card4)

    def test_eq_with_different_cards(self):
        """Test == operator with different cards."""
        self.assertFalse(self.card1 == self.card2)

    def test_eq_invalid_other(self):
        """Test == operator with invalid types."""
        with self.assertRaises(ValueError):
            self.card1 == "Hi"
        with self.assertRaises(ValueError):
            self.card1 == 5
        with self.assertRaises(ValueError):
            self.card1 == None
