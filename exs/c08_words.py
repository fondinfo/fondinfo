#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

text = "some bla bla stuff and then more bla bla stuff"
words = text.split(" ")

counts = {}  # try also collections.Counter
for w in words:
    counts[w] = counts.get(w, 0) + 1

for w, c in counts.items():
    print(w, c)
