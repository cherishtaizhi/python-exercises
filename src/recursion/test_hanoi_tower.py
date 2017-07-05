# -*- coding: utf-8 -*-

from . import hanoi_tower


def test_move_tower():
    height = 4
    src = [i for i in range(1, height+1)]
    dest = []
    expected_dest = src[:]
    buf = []

    hanoi_tower.move_tower(height, src, dest, buf)

    assert src == []
    assert dest == expected_dest
