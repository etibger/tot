# -*- coding: utf-8 -*-

from enum import Enum, auto
from random import shuffle, choice
from collections import Iterable

# __all__ = ['Card', 'Suit']


class Suit(Enum):
    Palace = auto()
    Library = auto()
    Garden = auto()
    Temple = auto()
    Stronghold = auto()
    NonSuit = auto()


_all_cards = []


class Win_Majority():
    def __init__(self, suit):
        self.suit = suit

    def __call__(self, plt, other):
        my_count = plt.get_num_of_suits(self.suit)
        other_count = other.get_num_of_suits(self.suit)
        if my_count > other_count:
            return 1
        if my_count == other_count and plt.win_ties and my_count != 0:
            return 1
        return 0


class For_Each_Point():
    def __init__(self, suit):
        self.suit = suit

    def __call__(self, plt, other):
        return plt.get_num_of_suits(self.suit)


class For_Each_NotOwn():
    def __call__(self, plt, other):
        s = 0
        for k, v in plt.crd_cnt.items():
            if k is not Suit.NonSuit:
                s += 1
        return 5 - s


class More_Single_Suit():
    def __call__(self, plt, other):
        my_cnt = plt.get_num_of_single()
        other_cnt = other.get_num_of_single()
        if my_cnt > other_cnt:
            return 1
        if my_cnt == other_cnt and plt.win_ties and my_cnt != 0:
            return 1
        return 0


class Win_Highest():
    def __call__(self, plt, other):
        if plt.max_point_win > other.max_point_win:
            return 1
        if (plt.max_point_win == other.max_point_win and plt.win_ties
                and plt.max_point_win != 0):
            return 1
        return 0


__card_raw_data__ = [
        [1, "Kings Nest", "Palace", "Win ties", None, None],
        [2, "Ancient Divide", "Palace", "Win majority of Stronghold",
            7, Win_Majority(Suit.Stronghold)],
        [3, "Eternal Palace", "Palace", "For each Library",
            3, For_Each_Point(Suit.Library)],
        [4, "The Great Library of Ahm", "Library", "Win majority of Temple",
            7, Win_Majority(Suit.Temple)],
        [5, "The Mana Well", "Library", "For each Set Palace,Stronghold,Temple",
            9, For_Each_Point([Suit.Palace, Suit.Stronghold, Suit.Temple])],
        [6, "The Citadel of the Prophets", "Library", "For each Garden",
            3, For_Each_Point(Suit.Garden)],
        [7, "Golden Ziggurat", "Garden", "Win majority of Palace",
            7, Win_Majority(Suit.Palace)],
        [8, "Gods Bath", "Garden", "For each Stronghold",
            3, For_Each_Point(Suit.Stronghold)],
        [9, "The Maze of the Damend", "Garden",
            "For each set Palace,Stronghold,Garden,Library,Temple",
            13, For_Each_Point([Suit.Palace, Suit.Stronghold, Suit.Garden,
                                Suit.Library, Suit.Temple])],
        [10, "The Eye of the North", "Stronghold", "For each NotOwn Suit",
            3, For_Each_NotOwn()],
        [11, "The Jinn Shackles", "Stronghold", "For each Stronghold",
            3, For_Each_Point(Suit.Stronghold)],
        [12, "Old Man's Pass", "Stronghold", "Win majority of Library",
            7, Win_Majority(Suit.Library)],
        [13, "Blood-tear Spring", "Temple", "Win majority of Gaden",
            7, Win_Majority(Suit.Garden)],
        [14, "The Sky Pillars", "Temple", "For each set Library,Garden",
            5, For_Each_Point([Suit.Library, Suit.Garden])],
        [15, "The Vestibule", "Temple", "For each Palace",
            3, For_Each_Point(Suit.Palace)],
        [16, "The Molehill", "NonSuit", "Win more SingleSuits",
            8, More_Single_Suit()],
        [17, "The Roof of the World", "NonSuit",
            "Double the most numerous Suits", None, None],
        [18, "The Sapphire Port", "NonSuit", "Win highest score",
            8, Win_Highest()]
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
        print("This is the Table before VP evaluation:\n{}".format(self))
        self.eval_vps()
        self.eval_highest()
        print("----------------------------------------------")

    def eval_non_vps(self):
        self.plt1.eval_non_vps()
        self.plt2.eval_non_vps()

    def eval_vps(self):
        self.plt1.eval_vps()
        self.plt2.eval_vps()

    def eval_highest(self):
        self.plt1.eval_highest()
        self.plt2.eval_highest()

    def get_other_plt(self, plt):
        return self.plt1 if plt is self.plt2 else self.plt2

    def get_other_num_of_suits(self, plt, suits):
        other_plt = self.plt1 if plt is self.plt2 else self.plt2
        return other_plt.get_num_of_suits(suits)


class PlayerTable():
    def __init__(self, table, name=None):
        self.cards = {}
        self.table = table
        self.win_ties = False
        self.name = name
        self.crd_cnt = {}
        self.max_point_win = 0
        self.vp = 0

    def place_card(self, card):
        self.cards[card.cid] = (card)
        self.crd_cnt[card.suit] = self.crd_cnt.get(card.suit, 0) + 1

    def remove_cards(self):
        tmp_crds = {k: v for (k, v) in self.cards.items() if v.frozen is False}
        self.cards = {k: v for (k, v) in self.cards.items() if v.frozen is True}
        self.crd_cnt = {}
        for k, v in self.cards.items():
            self.crd_cnt[v.suit] = self.crd_cnt.get(v.suit, 0) + 1

        self.win_ties = False
        self.max_point_win = 0
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
        s = "".join(
                ("\n{}:\n{}\n".format(self.name, self.crd_cnt),
                 "Win ties: {}\n".format(self.win_ties),
                 "\n".join(str(crd) for __, crd in self.cards.items())))
        return(s)

    def double_max(self):
        # print("Before dobuling: {}".format(self))
        # TODO change this to comprehension
        m = self.crd_cnt[max(self.crd_cnt, key=self.crd_cnt.get)]
        for k, v in self.crd_cnt.items():
            if self.crd_cnt[k] == m:
                self.crd_cnt[k] *= 2
        # print("After dobuling: {}".format(self))

    def eval_non_vps(self):
        # print("These are the Non Victory Point Cards:")
        for crd in (v for __, v in self.cards.items() if v.vp is None):
            if crd.cid == 1:
                self.win_ties = True
            if crd.cid == 17:
                self.double_max()
            print(crd)
        # print("{} : win_ties = {}\n".format(self.name, self.win_ties,))

    def eval_vps(self):
        for crd in (v for __, v in self.cards.items() if (v.vp is not None
                    and v.cid != 18)):
            tmp_vp = crd.vp * crd.evaluate(self, self.table.get_other_plt(self))
            print("I won {} points with card {}".format(tmp_vp, crd))
            if self.max_point_win < tmp_vp:
                self.max_point_win = tmp_vp
            self.vp += tmp_vp
        print("Total points after this round: {}".format(self.vp))

    def eval_highest(self):
        for __, crd in self.cards.items():
            if crd.cid == 18:
                print(crd)
                tmp_vp = crd.vp * crd.evaluate(self, self.table.get_other_plt(self))
                print("I won {} points with card {}".format(tmp_vp, crd))
                self.vp += tmp_vp

    def get_num_of_suits(self, suits=None):
        if isinstance(suits, Iterable) is False:
            suits = [suits]
        ns = []
        for suit in suits:
            ns.append(self.crd_cnt.get(suit, 0))
        return(min(ns))

    def get_num_of_single(self):
        s = 0
        for k, v in self.crd_cnt.items():
            if v == 1:
                s += 1
        return s


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
    def __init__(self, cid, name, suit, vp, evaluate):
        self.__cid = cid
        self.name = name
        self.suit = suit
        self.vp = vp
        self.frozen = False
        self.evaluate = evaluate

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
        _all_cards.append(Card(crd[0], crd[1], Suit[crd[2]], crd[4], crd[5]))


def del_cards():
    for crd in _all_cards:
        crd.frozen = False


def print_all_cards():
    for crd in _all_cards:
        print(crd)
