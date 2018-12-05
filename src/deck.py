from constants import DeckType, Suit, HalfSuit, FaceValue
from card import Card


class Deck:
    def __init__(self, deck_type):
        self.cards = []
        self.deck_type = deck_type
        initializer = {
            DeckType.STANDARD: self.initialize_as_standard_deck
        }
        initializer.get(deck_type)()

    def initialize_as_standard_deck(self):
        for fv in FaceValue:
            if fv.value < 2 or fv.value == 8:
                if fv.value == 8:
                    for s in Suit:
                        if s != Suit.JOKER:
                            card = Card(fv, s, HalfSuit.JOKER)
                            self.cards.append(card)
                else:
                    card = Card(fv, Suit.JOKER, HalfSuit.JOKER)
                    self.cards.append(card)
            else:
                if 2 <= fv.value <= 7:
                    for s in Suit:
                        if s != Suit.JOKER:
                            card = Card(fv, s, HalfSuit.LOWER)
                            self.cards.append(card)
                else:
                    for s in Suit:
                        if s != Suit.JOKER:
                            card = Card(fv, s, HalfSuit.HIGHER)
                            self.cards.append(card)


if __name__ == "__main__":
    d = Deck(DeckType.STANDARD)
