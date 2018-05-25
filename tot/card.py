# -*- coding: utf-8 -*-

from enum import Enum, auto
from random import shuffle, choice

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
        self.plt1 = PlayerTable(table=self, name="plt1")
        self.plt2 = PlayerTable(table=self, name="plt2")

    def __str__(self):
        s = str(self.plt1) + str(self.plt2)
        return s

    def evaluate_table(self):
        self.eval_non_vps()
        self.eval_vps()

    def eval_non_vps(self):
        self.plt1.eval_non_vps()
        self.plt2.eval_non_vps()

    def eval_vps(self):
        pass


class PlayerTable():
    def __init__(self, table, name=None):
        self.cards = {}
        self.table = table
        self.win_ties = False
        self.double_max = False
        self.name = name
        self.crd_cnt = {}

    def place_card(self, card):
        self.cards[card.cid] = (card)
        self.crd_cnt[card.suit] = self.crd_cnt.get(card.suit, 0) + 1

    def remove_cards(self):
        tmp_crds = {k: v for (k, v) in self.cards.items() if v.frozen is False}
        self.cards = {k: v for (k, v) in self.cards.items() if v.frozen is True}
        self.crd_cnt = {}
        for k, v in self.cards.items():
            self.crd_cnt[v.suit] = self.crd_cnt.get(v.suit, 0) + 1

        return tmp_crds

    def discard_card(self, cid):
        self.cards.pop(cid)
        # card = self.cards.pop(cid)
        # print("[PLT - {}]: {} is discarded".format(self.name, card))

    def freeze_card(self, cid):
        self.cards[cid].freeze()

    def choose_random(self):
        return choice(list(self.cards.keys()))

    def choose_smallest(self):
        return min(list(self.cards.keys()))

    def choose_largest(self):
        return max(list(self.cards.keys()))

    def __str__(self):
        s = "".join(("{}:\n{}\n".format(self.name, self.crd_cnt),
                    "\n".join(str(crd) for __, crd in self.cards.items())))
        return(s)

    def eval_non_vps(self):
        self.win_ties = False
        print("These are the Non Victory Point Cards:")
        for crd in (v for __, v in self.cards.items() if v.vp is None):
            if crd.cid == 1:
                self.win_ties = True
            if crd.cid == 17:
                self.double_max = True
            print(crd)
        print("{} : win_ties = {}, double_max = {}\n".format(
            self.name, self.win_ties, self.double_max))


class Deck():
    def __init__(self):
        self.deck = list(range(18, 0, -1))

    def shuffle(self):
        shuffle(self.deck)

    def pop(self):
        return _all_cards[self.deck.pop()-1]


class Hand():
    def __init__(self):
        self.cards = {}

    def pull_card(self, card):
        self.cards[card.cid] = card

    def place_card(self, cid):
        return self.cards.pop(cid)

    def place_rand(self):
        return self.place_card(choice(list(self.cards.keys())))

    def place_smallest(self):
        return self.place_card(min(list(self.cards.keys())))

    def __str__(self):
        s = "\n".join(str(crd) for __, crd in self.cards.items())
        return(s)


class Card():
    """
    Store every relevant attribute about the ToT cards.
    """
    def __init__(self, cid, name, suit, vp):
        self.__cid = cid
        self.name = name
        self.suit = suit
        self.vp = vp
        self.frozen = False

    @property
    def cid(self):
        """
        cid is private property to as this is used to create hash and hence
        needs to be unchanged.
        """
        return self.__cid

    def __str__(self):
        s = "cid: {_Card__cid}, name: {name}, suit: {suit.name}, vp: {vp}".format(**self.__dict__)
        if self.frozen:
            s = "* " + s
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


def generate_cards():
    for crd in __card_raw_data__:
        _all_cards.append(Card(crd[0], crd[1], Suit[crd[2]], crd[4]))


def del_cards():
    for crd in _all_cards:
        crd.frozen = False


def print_all_cards():
    for crd in _all_cards:
        print(crd)
