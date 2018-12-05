from deck import Deck
from constants import DeckType
import unittest


class Tests(unittest.TestCase):
    def test_standard_deck(self):
        d = Deck(DeckType.STANDARD)
        print(d.cards)
        self.assertTrue(d)
        self.assertTrue(d.cards)
        self.assertEqual(len(d.cards), 54)


if __name__ == '__main__':
    unittest.main()
