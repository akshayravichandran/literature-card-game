from card import Card
from constants import DeckType, Suit, HalfSuit, FaceValue
import random

class Deck:
    def __init__(self, deck_type):
        self.cards = []
        self.deck_type = deck_type
        initializer = {
            DeckType.STANDARD: self.initialize_as_standard_deck
        }
        initializer.get(deck_type)()

    def initialize_as_standard_deck(self):
        # Build a deck of 54 cards with 9 half-suits
        for fv in FaceValue:
            # RED JOKER, BLACK JOKER and all 8s form the JOKER half-suit
            # RED and BLACK are defined as face values 0 and 1
            if fv.value < 2 or fv.value == 8:
                if fv.value == 8:
                    for s in Suit:
                        # ignore the JOKER suit (not to be confused with the JOKER half-suit)
                        if s != Suit.JOKER:
                            self.cards.append(Card(fv, s, HalfSuit.JOKER))
                else:
                    # JOKER suit cards
                    self.cards.append(Card(fv, Suit.JOKER, HalfSuit.JOKER))
            else:
                if 2 <= fv.value <= 7:
                    # LOWER half-suits
                    for s in Suit:
                        if s != Suit.JOKER:
                            self.cards.append(Card(fv, s, HalfSuit.LOWER))
                else:
                    # UPPER half-suits
                    for s in Suit:
                        if s != Suit.JOKER:
                            self.cards.append(Card(fv, s, HalfSuit.HIGHER))

    def shuffle(self):
        random.shuffle(self.cards)
