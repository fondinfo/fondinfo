#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

n = int(input("n? "))
total = 0
for i in range(1, n + 1):
    total += i

print("The sum is", total)
print("Gauss’ formula is", total == n * (n + 1) / 2)
