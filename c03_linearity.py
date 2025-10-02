#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

n = int(input("Rounds (>1)? "))  # try with 5

first = float(input("First value? "))  # try with 10
last = float(input("Last value? "))    # try with 15

delta = (last - first) / (n - 1)
print("Delta :", delta)

for i in range(n):
    v = i * delta + first
    print("Round", i + 1, ":", v)
