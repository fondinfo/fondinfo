#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import unittest

from boardgame import BoardGame, print_game
from c09_fifteen import Fifteen

MOVES = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def tiles(game: BoardGame) -> list[int]:
    """All the tiles, row after row. The blank is the number cols * rows."""
    cols, rows = game.cols(), game.rows()
    return [int(game.read(x, y) or cols * rows)
            for y in range(rows) for x in range(cols)]


def blank(game: BoardGame) -> tuple[int, int]:
    for y in range(game.rows()):
        for x in range(game.cols()):
            if game.read(x, y) == "":
                return x, y
    raise ValueError("No blank cell")


class FifteenTest(unittest.TestCase):
    """Tests of the game Fifteen."""

    def test_shuffled_board(self):
        for w, h in [(2, 2), (3, 2), (4, 4)]:
            with self.subTest(size=(w, h)):
                game = self.make_game(w, h)
                self.assertEqual((game.cols(), game.rows()), (w, h))
                self.assertEqual(sorted(tiles(game)), list(range(1, w * h + 1)))
                self.assertEqual(game.read(w - 1, h - 1), "1")
                self.assertFalse(game.finished())
                self.assertEqual(game.status(), "Playing")

    def test_read_outside(self):
        game = self.make_game(3, 2)
        for x, y in [(-1, 0), (3, 0), (0, -1), (0, 2)]:
            self.assertEqual(game.read(x, y), "")

    def test_slide(self):
        game = self.make_game(3, 3)
        for dx, dy in MOVES:
            bx, by = blank(game)
            x, y = bx + dx, by + dy
            if 0 <= x < 3 and 0 <= y < 3:
                tile = game.read(x, y)
                game.play(x, y, "flag")  # the action is not used
                self.assertEqual(game.read(bx, by), tile)
                self.assertEqual(game.read(x, y), "")

    def test_ignored_plays(self):
        game = self.make_game(3, 3)
        before = tiles(game)
        bx, by = blank(game)
        for x, y in [(bx, by), (bx + 1, by + 1), (bx + 2, by),
                     (-1, 0), (0, 3), (3, 3)]:
            game.play(x, y, "")
        self.assertEqual(tiles(game), before)

    def test_one_cell_board(self):
        game = self.make_game(1, 1)
        self.assertTrue(game.finished())
        self.assertEqual(game.status(), "Puzzle solved!")
        self.assertEqual(game.read(0, 0), "")

    def make_game(self, w: int, h: int) -> BoardGame:
        return Fifteen(w, h)


if __name__ == "__main__":
    unittest.main()
