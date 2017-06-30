# -*- coding: utf-8 -*-

def move_tower(height, src, dest, buf):
    src[:], dest[:] = dest[:], src[:]
