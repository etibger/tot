# -*- coding: utf-8 -*-
import pytest
from tot.card import Card, Suit

def test_card_singleton():
    """
    Test that the card is really a singleton. No two different instance should be
    created.
    """
    c1 = Card(1, "first name", Suit.Palace)
    c2 = Card(1, "first name", Suit.Palace)
    assert c1 is c2

def test_card_print():
    """
    Test that the print method prints the expected format.
    """
    c1 = Card(1, "first name", Suit.Palace)
    assert str(c1) == 'number: 1, name: first name, suit: Suit.Palace'

def test_card_immutable():
    with pytest.raises(AttributeError):
        c1 = Card(1, "first name", Suit.Palace)
        c1.name = "modify this"

def test_lt_hash():
    """
    Test that less than comparision works. It raises TypeError when comparing to a
    non-Card class. Test if equality check works with the updated hash function.
    """
    c1 = Card(1, "1", Suit.Palace)
    c2 = Card(2, "2", Suit.Palace)
    assert c1 < c2
    with pytest.raises(TypeError):
        c1 < 1
    c3 = Card(1, "1", Suit.Palace)
    assert c1 is c3
    assert c1 == c3
