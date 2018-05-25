# -*- coding: utf-8 -*-

from enum import Enum, auto
from random import shuffle

# __all__ = ['Card', 'Suit']


class Suit(Enum):
    Palace = auto()
    Library = auto()
    Garden = auto()
    Temple = auto()
    Stronghold = auto()
    NonSuit = auto()


_all_cards = []


__card_raw_data__ = [
        [1, "Kings Nest", "Palace", "Win ties", None],
        [2, "Ancient Divide", "Palace", "Win majority of Stronghold", 7],
        [3, "Eternal Palace", "Palace", "For each Library", 3],
        [4, "The Great Library of Ahm", "Library", "Win majority of Temple", 7],
        [5, "The Mana Well", "Library", "For each Set Palace,Stronghold,Temple", 9],
        [6, "The Citadel of the Prophets", "Library", "For each Garden", 3],
        [7, "Golden Ziggurat", "Garden", "Win majority of Palace", 7],
        [8, "Gods Bath", "Garden", "For each Stronghold", 3],
        [9, "The Maze of the Damend", "Garden",
            "For each set Palace,Stronghold,Garden,Library,Temple", 13],
        [10, "The Eye of the North", "Stronghold", "For each NotOwn Suit", 3],
        [11, "The Jinn Shackles", "Stronghold", "For each Stronghold", 3],
        [12, "Old Man's Pass", "Stronghold", "Win majority of Library", 7],
        [13, "Blood-tear Spring", "Temple", "Win majority of Gaden", 7],
        [14, "The Sky Pillars", "Temple", "For each set Library,Garden", 5],
        [15, "The Vestibule", "Temple", "For each Palace", 3],
        [16, "The Molehill", "NonSuit", "Win more SingleSuits", 8],
        [17, "The Roof of the World", "NonSuit",
            "Double the most numerous Suits", None],
        [18, "The Sapphire Port", "NonSuit", "Win highest score", 8]
    ]


class Table():
    def __init__(self):
        self.cards = {}
        self.win_ties = False

    def place_card(self, card):
        self.cards[card.cid] = (card)

    def remove_cards(self):
        tmp_crds = {k: v for (k, v) in self.cards.items() if v.frozen is False}
        self.cards = {k: v for (k, v) in self.cards.items() if v.frozen is True}
        return tmp_crds

    def __str__(self):
        s = "\n".join(str(crd) for crd in self.cards)
        return(s)


class Deck():
    def __init__(self):
        self.deck = list(range(1, 18))
        shuffle(self.deck)

    def pop(self):
        return self.deck.pop()


class Hand():
    def __init__(self):
        self.cards = {}

    def pull_card(self, card):
        self.cards[card.cid] = card

    def place_card(self, cid):
        return self.cards.pop(cid)


class Card():
    """
    Store every relevant attribute about the ToT cards.
    """
    def __init__(self, cid, name, suit):
        self.__cid = cid
        self.name = name
        self.suit = suit
        self.frozen = False

    @property
    def cid(self):
        """
        cid is private property to as this is used to create hash and hence
        needs to be unchanged.
        """
        return self.__cid

    def __str__(self):
        s = "cid: {_Card__cid}, name: {name}, suit: {suit.name}".format(**self.__dict__)
        return s

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.cid < other.cid
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.cid == other.cid
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.cid)

    def freeze(self):
        self.frozen = True

    @staticmethod
    def _find_id_in_card_list(number, card_list):
        """
        Searches for the card number in the given card_list and returns it's index
        if found and None when not.
        """
        # TODO add proper description

        tmp_crd = next(filter(lambda x: x[1].number == number, enumerate(card_list)), (None, None))
        return tmp_crd[0]


def generate_cards():
    for crd in __card_raw_data__:
        _all_cards.append(Card(crd[0], crd[1], Suit[crd[2]]))


def print_all_cards():
    for crd in _all_cards:
        print(crd)
