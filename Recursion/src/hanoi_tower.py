# -*- coding: utf-8 -*-

def move_tower(h, s, d, b):
    if h >= 1:
        move_tower(h-1, s, b, d)
        d.insert(0, s.pop(0))
        move_tower(h-1, b, d, s)
