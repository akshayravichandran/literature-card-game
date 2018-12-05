from enum import Enum, auto, unique


@unique
class DeckType(Enum):
    STANDARD = auto()   # 54 cards. 2-7 lower half-suit. 9-A higher half-suit. All 8s and 2 jokers are joker half-suit.


@unique
class FaceValue(Enum):
    RED = 0
    BLACK = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


@unique
class Suit(Enum):
    CLUB = auto()
    DIAMOND = auto()
    HEART = auto()
    SPADE = auto()
    JOKER = auto()


@unique
class HalfSuit(Enum):
    LOWER = auto()
    HIGHER = auto()
    JOKER = auto()
