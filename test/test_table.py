# -*- coding: utf-8 -*-
# import pytest
from heapq import nsmallest
from tot.card import generate_cards, Table, Deck, Hand, print_all_cards
# from tot.card import _all_cards


def test_simple_game():
    assert simple_game() is True


def simple_game():
    generate_cards()
    print_all_cards()
    t1 = Table()
    d = Deck()
#    print("Size of Deck: {}".format(len(d.deck)))
    plt1 = t1.plt1
    plt2 = t1.plt2
    h1 = Hand()
    h2 = Hand()
    # Pull card from deck iteratively
    for i in range(5):
        h1.pull_card(d.pop())
        h2.pull_card(d.pop())

    for i in range(5):
        # print("\n-------------------------------------")
        # print("{}'th round:".format(i))
        # print("Hand1: ")
        # print(h1)
        # print("Hand2: ")
        # print(h2)
        # Choose a card an place it to the table simultaneously
        plt1.place_card(h1.place_smallest())
        plt2.place_card(h2.place_smallest())
        # print(plt1)
        # print(plt2)
        # swap hands
        h1, h2 = h2, h1

    # choose a card to discard
    plt1.discard_card(plt1.choose_largest())
    plt2.discard_card(plt2.choose_largest())
    # choose a card to freeze
    plt1.freeze_card(plt1.choose_smallest())
    plt2.freeze_card(plt2.choose_smallest())

    # print("After freezing and discarding")
    # print(plt1)
    # print(plt2)

    # print("After collecting the cards from the table")
    # Pick up the remaining unfrozen cards
    h1.cards = plt1.remove_cards()
    h2.cards = plt2.remove_cards()
    # print(plt1)
    # print(plt2)
    # print("Hand1: ")
    # print(h1)
    # print("Hand2: ")
    # print(h2)

    # pull 2 cards iteratively, to fill up to 5 cards in hand
    for i in range(2):
        h1.pull_card(d.pop())
        h2.pull_card(d.pop())

    # place 5 cards
    for i in range(5):
        # print("\n-------------------------------------")
        # print("{}'th round:".format(i))
        # print("Hand1: ")
        # print(h1)
        # print("Hand2: ")
        # print(h2)
        plt1.place_card(h1.place_smallest())
        plt2.place_card(h2.place_smallest())
        # print(plt1)
        # print(plt2)
        h1, h2 = h2, h1

    # choose a card to discard
    plt1.discard_card(plt1.choose_largest())
    plt2.discard_card(plt2.choose_largest())

    # choose a card to freeze
    plt1.freeze_card(nsmallest(2, list(plt1.cards.keys()))[-1])
    plt2.freeze_card(nsmallest(2, list(plt2.cards.keys()))[-1])

    # print("After freezing and discarding")
    # print(plt1)
    # print(plt2)

    # print("After collecting the cards from the table")
    # pick up the remaining unfrozen cards
    h1.cards = plt1.remove_cards()
    h2.cards = plt2.remove_cards()
    # print(plt1)
    # print(plt2)
    # print("Hand1: ")
    # print(h1)
    # print("Hand2: ")
    # print(h2)

    # draw 2 cards to top up to 5
    for i in range(2):
        h1.pull_card(d.pop())
        h2.pull_card(d.pop())

    # place 5 cards iteratively and swap hands between them
    for i in range(5):
        # print("\n-------------------------------------")
        # print("{}'th round:".format(i))
        # print("Hand1: ")
        # print(h1)
        # print("Hand2: ")
        # print(h2)
        plt1.place_card(h1.place_smallest())
        plt2.place_card(h2.place_smallest())
        # print(plt1)
        # print(plt2)
        h1, h2 = h2, h1

    if len(d.deck) == 0:
        print("test pass")
        return True
    return False


if __name__ == "__main__":
    simple_game()
