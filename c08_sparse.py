#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import random, choice

a = {(0, 0): 5, (1, 1): 8, (2, 0): -2}
b = {(1, 1): -8, (2, 0): 3, (0, 2): 4}

def random_sparse(w, h):
    """Random sparse matrix: ~40% filled, values ±1, ±2."""
    m = {}
    for y in range(h):
        for x in range(w):
            if random() < 0.4:
                m[(x, y)] = choice([-2, -1, 1, 2])
    return m

def main():
    values = {(0, 0): 5, (1, 1): 8,
              (2, 2): 3, (1, 3): 6}  # dict[(int, int), int]

    x = int(input("Col? "))
    y = int(input("Row? "))
    val = values.get((x, y), 0)  # key not found → default 0
    print(val)

if __name__ == "__main__":
    main()
