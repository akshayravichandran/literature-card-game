from deck import Deck
from constants import DeckType
import unittest


class Tests(unittest.TestCase):

    seed = 0

    def test_standard_deck(self):
        d = Deck(DeckType.STANDARD)
        self.assertTrue(d)
        self.assertTrue(d.cards)
        self.assertEqual(len(d.cards), 54)

    def test_shuffled_deck(self):
        deck = Deck(DeckType.STANDARD)
        shuffled_deck = Deck(DeckType.STANDARD)
        shuffled_deck.shuffle(self.seed)
        self.assertNotEqual(deck.cards, shuffled_deck.cards)


if __name__ == '__main__':
    unittest.main()
