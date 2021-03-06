class Card:
    def __init__(self, face_value, suit, half_suit):
        self.face_value = face_value
        self.suit = suit
        self.half_suit = half_suit

    def __str__(self):
        return str(self.face_value, self.suit, self.half_suit)

    def __eq__(self, other):
        return self.face_value == other.face_value and self.suit == other.suit and self.half_suit == other.half_suit
