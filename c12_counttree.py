#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

T = int | list["T"]

def count_tree(t: T) -> int:
    if not isinstance(t, list):
        return 1
    # return sum(count_tree(v) for v in t)
    count = 0
    for v in t:
        count += count_tree(v)
    return count

tree = [[1, 2, [3, 4], [5]], 6]
print(count_tree(tree))
