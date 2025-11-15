#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from actor import Actor, Arena

class Mario(Actor):
    def __init__(self):
        self._x, self._y = 0, 240
        self._w, self._h = 20, 20
        self._dx, self._dy = 0, 0
        self._speed, self._jump = 2, -8
        self._gravity = 0.25

    def move(self, arena):
        keys = arena.current_keys()
        self._dx = 0
        if "ArrowRight" in keys:
             self._dx = self._speed
        elif "ArrowLeft" in keys:
             self._dx = -self._speed
        for other in arena.collisions():
            sx, sy, sw, sh = self.pos() + self.size()  # self's pos
            ox, oy, ow, oh = other.pos() + other.size()  # other's pos

            # move to the nearest border: left, right, top or bottom
            move_x = min(ox - sx - sw, ox + ow - sx, key=abs)
            move_y = min(oy - sy - sh, oy + oh - sy, key=abs)
            if abs(move_x) < abs(move_y):
                self._x += move_x
                self._dx = 0
            elif move_y != 0:
                self._y += move_y
                self._dy = 0
                if sy < oy and "ArrowUp" in keys:  # if on top, can jump
                    self._dy = self._jump

        arena_w, arena_h = arena.size()
        self._x = (self._x + self._dx) % arena_w
        self._y += self._dy
        self._dy += self._gravity

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return None


class Wall(Actor):
    def __init__(self, pos, size):
        self._pos = pos
        self._size = size

    def move(self, arena):
        return

    def pos(self):
        return self._pos

    def size(self):
        return self._size

    def sprite(self):
        return None


def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        g2d.draw_rect(a.pos(), a.size())

    arena.tick(g2d.current_keys())


arena = Arena((640, 480))
arena.spawn(Wall((240, 350), (100, 40)))
arena.spawn(Wall((420, 250), (100, 40)))
arena.spawn(Wall((0, 460), (640, 20)))
arena.spawn(Mario())

g2d.init_canvas(arena.size())
g2d.main_loop(tick)
