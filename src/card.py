class Card:
    def __init__(self, face_value, suit, half_suit):
        self.face_value = face_value
        self.suit = suit
        self.half_suit = half_suit

    def __str__(self):
        return str(self.face_value) + str(self.suit) +  str(self.half_suit)

    def __repr__(self):
        return str(self.face_value).split('.')[1] \
        + "_" + str(self.suit).split('.')[1] \
        + "_" + str(self.half_suit).split('.')[1]

    def __eq__(self, other):
        return self.face_value == other.face_value and self.suit == other.suit and self.half_suit == other.half_suit

    def __hash__(self):
        return id(self)