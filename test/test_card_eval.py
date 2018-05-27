# -*- coding: utf-8 -*-
from tot.card import generate_cards, Table, _all_cards


def test_scenario_0():
    """
    Check win for each single cards.
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[2])
    t1.plt1.place_card(_all_cards[5])
    t1.plt1.place_card(_all_cards[7])
    t1.plt1.place_card(_all_cards[10])
    t1.plt1.place_card(_all_cards[14])
    print(t1.plt1)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    t1.plt1.eval_vps()
    t1.plt1.eval_highest()
    assert t1.plt1.vp == 5*3
    assert t1.plt1.max_point_win == 3


def test_scenario_1():
    """
    Check win for each set cards, and win tie setting. Card removal resets win ties
    and max point win.
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[4])
    t1.plt1.place_card(_all_cards[8])
    t1.plt1.place_card(_all_cards[13])
    t1.plt1.place_card(_all_cards[10])
    t1.plt1.place_card(_all_cards[0])
    print(t1.plt1)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    assert t1.plt1.win_ties is True
    t1.plt1.eval_vps()
    t1.plt1.eval_highest()
    assert t1.plt1.vp == 9+13+5+3
    assert t1.plt1.max_point_win == 13
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


def test_scenario_2():
    """
    Same as scenario 1 but doubling the highest count
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[4])
    t1.plt1.place_card(_all_cards[8])
    t1.plt1.place_card(_all_cards[13])
    t1.plt1.place_card(_all_cards[10])
    t1.plt1.place_card(_all_cards[0])
    t1.plt1.place_card(_all_cards[16])
    print(t1.plt1)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    assert t1.plt1.win_ties is True
    t1.plt1.eval_vps()
    t1.plt1.eval_highest()
    assert t1.plt1.vp == (9+13+5+3)*2
    assert t1.plt1.max_point_win == 26
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


def test_scenario_3():
    """
    Win majority check: Normal winning
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[1])
    t1.plt1.place_card(_all_cards[10])
    t1.plt2.place_card(_all_cards[3])
    print(t1.plt1)
    print(t1.plt2)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    t1.plt2.eval_non_vps()
    assert t1.plt1.win_ties is False
    t1.plt1.eval_vps()
    t1.plt2.eval_vps()
    t1.plt1.eval_highest()
    t1.plt2.eval_highest()
    assert t1.plt1.vp == 7+3
    assert t1.plt1.max_point_win == 7
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


def test_scenario_4():
    """
    Win majority check: Normal Losing
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[1])
    t1.plt2.place_card(_all_cards[10])
    t1.plt2.place_card(_all_cards[3])
    print(t1.plt1)
    print(t1.plt2)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    t1.plt2.eval_non_vps()
    assert t1.plt1.win_ties is False
    t1.plt1.eval_vps()
    t1.plt2.eval_vps()
    t1.plt1.eval_highest()
    t1.plt2.eval_highest()
    assert t1.plt1.vp == 0
    assert t1.plt1.max_point_win == 0
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


def test_scenario_5():
    """
    Win majority check: Losing by Tie
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[1])
    t1.plt1.place_card(_all_cards[11])
    t1.plt2.place_card(_all_cards[10])
    t1.plt2.place_card(_all_cards[3])
    print(t1.plt1)
    print(t1.plt2)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    t1.plt2.eval_non_vps()
    assert t1.plt1.win_ties is False
    t1.plt1.eval_vps()
    t1.plt2.eval_vps()
    t1.plt1.eval_highest()
    t1.plt2.eval_highest()
    assert t1.plt1.vp == 0
    assert t1.plt1.max_point_win == 0
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


def test_scenario_6():
    """
    Win majority check: Winning by Tie
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[1])
    t1.plt1.place_card(_all_cards[0])
    t1.plt1.place_card(_all_cards[11])
    t1.plt2.place_card(_all_cards[10])
    t1.plt2.place_card(_all_cards[3])
    print(t1.plt1)
    print(t1.plt2)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    t1.plt2.eval_non_vps()
    assert t1.plt1.win_ties is True
    t1.plt1.eval_vps()
    t1.plt2.eval_vps()
    t1.plt1.eval_highest()
    t1.plt2.eval_highest()
    assert t1.plt1.vp == 7
    assert t1.plt1.max_point_win == 7
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


def test_scenario_7():
    """
    Win More Single suit with tie
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[1])
    t1.plt1.place_card(_all_cards[0])
    t1.plt1.place_card(_all_cards[11])
    t1.plt1.place_card(_all_cards[15])
    t1.plt2.place_card(_all_cards[10])
    t1.plt2.place_card(_all_cards[3])
    print(t1.plt1)
    print(t1.plt2)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    t1.plt2.eval_non_vps()
    assert t1.plt1.win_ties is True
    t1.plt1.eval_vps()
    t1.plt2.eval_vps()
    t1.plt1.eval_highest()
    t1.plt2.eval_highest()
    assert t1.plt1.vp == 7+8
    assert t1.plt1.max_point_win == 8
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


def test_scenario_7_1():
    """
    Win More Single suit normally
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[1])
    t1.plt1.place_card(_all_cards[0])
    t1.plt1.place_card(_all_cards[11])
    t1.plt1.place_card(_all_cards[15])
    t1.plt2.place_card(_all_cards[10])
    print(t1.plt1)
    print(t1.plt2)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    t1.plt2.eval_non_vps()
    assert t1.plt1.win_ties is True
    t1.plt1.eval_vps()
    t1.plt2.eval_vps()
    t1.plt1.eval_highest()
    t1.plt2.eval_highest()
    assert t1.plt1.vp == 7+8
    assert t1.plt1.max_point_win == 8
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


def test_scenario_8():
    """
    Win Highest with tie
    """
    generate_cards()
    t1 = Table()
    t1.plt1.place_card(_all_cards[1])
    t1.plt1.place_card(_all_cards[0])
    t1.plt1.place_card(_all_cards[11])
    t1.plt1.place_card(_all_cards[17])
    t1.plt2.place_card(_all_cards[12])
    t1.plt2.place_card(_all_cards[3])
    print(t1.plt1)
    print(t1.plt2)
    assert t1.plt1.max_point_win == 0
    assert t1.plt1.vp == 0
    assert t1.plt1.win_ties is False
    t1.plt1.eval_non_vps()
    t1.plt2.eval_non_vps()
    assert t1.plt1.win_ties is True
    t1.plt1.eval_vps()
    t1.plt2.eval_vps()
    t1.plt1.eval_highest()
    t1.plt2.eval_highest()
    assert t1.plt1.vp == 7+8
    assert t1.plt1.max_point_win == 7
    t1.plt1.remove_cards()
    assert t1.plt1.win_ties is False
    assert t1.plt1.max_point_win == 0


if __name__ == '__main__':
    test_scenario_8()
