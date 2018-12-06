from deck import Deck
from constants import DeckType
import unittest


class Tests(unittest.TestCase):

    seed = 0

    def test_standard_deck(self):
        d = Deck(DeckType.STANDARD)
        self.assertTrue(d, "Deck not initialized")
        self.assertTrue(d.cards, "No cards initialized")
        self.assertEqual(len(d.cards), 54, "Number of cards in deck is not 54")

    def test_shuffled_deck(self):
        deck = Deck(DeckType.STANDARD)
        shuffled_deck = Deck(DeckType.STANDARD)
        shuffled_deck.shuffle(self.seed)
        self.assertNotEqual(deck.cards, shuffled_deck.cards, "Un-shuffled and shuffled decks are equal")


if __name__ == '__main__':
    unittest.main()
