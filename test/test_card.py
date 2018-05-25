# -*- coding: utf-8 -*-
import pytest
from tot.card import Card, Suit, generate_cards, _all_cards


def test_card_print():
    """
    Test that the print method prints the expected format.
    """
    c1 = Card(1, "first name", Suit.Palace, 3)
    assert str(c1) == 'cid: 1, name: first name, suit: Palace, vp: 3'


def test_card_immutable():
    with pytest.raises(AttributeError):
        c1 = Card(1, "first name", Suit.Palace, 3)
        c1.cid = "modify this"


def test_lt_hash():
    """
    Test that less than comparision works. It raises TypeError when comparing to a
    non-Card class. Test if equality check works with the updated hash function.
    """
    c1 = Card(1, "1", Suit.Palace, 3)
    c2 = Card(2, "2", Suit.Palace, 3)
    assert c1 < c2
    with pytest.raises(TypeError):
        c1 < 1
    assert c1 != 2
    c3 = Card(1, "1", Suit.Palace, 3)
    assert c1 == c3

    a = {}
    a[c1] = 1


def test_all_cards():
    generate_cards()
    assert len(_all_cards) == 18
    assert _all_cards[3].suit == Suit.Library and _all_cards[3].cid == 4
    tmp_suit = ['Palace', 'Library', 'Garden', 'Stronghold', 'Temple', 'NonSuit']
    for i, crd in enumerate(_all_cards):
        assert crd.cid == i+1
        assert crd.suit == Suit[tmp_suit[i//3]]


# TODO check hash function of card
