from enum import Enum


class Suit(Enum):
    spade = "s"
    heart = "h"
    club = "c"
    diamond = "d"


class Rank(Enum):
    ace = "a"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"
    ten = "t"
    jack = "j"
    queen = "q"
    king = "k"


class Card:
    """
    扑克牌类
    """

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit.value}{self.rank.value}"

    def __eq__(self, other):
        other: Card
        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self):
        return hash(self.suit) ^ hash(self.rank)


class Hand(set):
    """
    手牌类型
    """


class Deck(set):
    """
    牌库类
    """

    def createDeck(self):
        for r in Rank:
            for s in Suit:
                self.add(Card(s, r))
        return self




