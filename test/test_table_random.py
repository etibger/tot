# -*- coding: utf-8 -*-
# import pytest
from tot.card import generate_cards, del_cards, Table, Deck, Hand, print_all_cards
# from tot.card import _all_cards


def test_rand_game():
    assert rand_game() is True


def rand_game():
    del_cards()
    generate_cards()
    print_all_cards()
    print("\n")
    t1 = Table()
    d = Deck()
    d.shuffle()
    # print("Size of Deck: {}".format(len(d.deck)))
    plt1 = t1.plt1
    plt2 = t1.plt2
    h1 = Hand()
    h2 = Hand()
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
        plt1.place_card(h1.place_rand())
        plt2.place_card(h2.place_rand())
        # print(plt1)
        # print(plt2)
        h1, h2 = h2, h1

    print("First turn:")
    # print(t1)
    t1.evaluate_table()

    plt1.discard_card(plt1.choose_random())
    plt2.discard_card(plt2.choose_random())
    plt1.freeze_card(plt1.choose_random())
    plt2.freeze_card(plt2.choose_random())

    # print("After freezing and discarding")
    # print(t1)

    # print("After collecting the cards from the table")
    h1.cards = plt1.remove_cards()
    h2.cards = plt2.remove_cards()
    # print(plt1)
    # print(plt2)
    # print("Hand1: ")
    # print(h1)
    # print("Hand2: ")
    # print(h2)

    for i in range(2):
        h1.pull_card(d.pop())
        h2.pull_card(d.pop())

    for i in range(5):
        # print("\n-------------------------------------")
        # print("{}'th round:".format(i))
        # print("Hand1: ")
        # print(h1)
        # print("Hand2: ")
        # print(h2)
        plt1.place_card(h1.place_rand())
        plt2.place_card(h2.place_rand())
        # print(plt1)
        # print(plt2)
        h1, h2 = h2, h1

    print("Second turn:")
    # print(t1)
    t1.evaluate_table()

    cid = plt1.choose_random()
    while plt1.cards[cid].frozen is True:
        cid = plt1.choose_random()
    plt1.discard_card(cid)

    cid = plt2.choose_random()
    while plt2.cards[cid].frozen is True:
        cid = plt2.choose_random()
    plt2.discard_card(cid)

    plt1.freeze_card(plt1.choose_random())
    plt2.freeze_card(plt2.choose_random())

    # print("After freezing and discarding")
    # print(plt1)
    # print(plt2)

    # print("After collecting the cards from the table")
    h1.cards = plt1.remove_cards()
    h2.cards = plt2.remove_cards()
    # print(plt1)
    # print(plt2)
    # print("Hand1: ")
    # print(h1)
    # print("Hand2: ")
    # print(h2)

    for i in range(2):
        h1.pull_card(d.pop())
        h2.pull_card(d.pop())

    for i in range(5):
        # print("\n-------------------------------------")
        # print("{}'th round:".format(i))
        # print("Hand1: ")
        # print(h1)
        # print("Hand2: ")
        # print(h2)
        plt1.place_card(h1.place_rand())
        plt2.place_card(h2.place_rand())
        # print(plt1)
        # print(plt2)
        h1, h2 = h2, h1

    print("Third turn:")
    # print(t1)
    t1.evaluate_table()

    if len(d.deck) == 0:
        # print("test pass")
        return True
    return False


if __name__ == "__main__":
    rand_game()
