#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

N = 26  # ord('Z') - ord('A') + 1
counters = [0] * N

text = input('text? ')

for c in text:
    if 'A' <= c <= 'Z':
        index = ord(c) - ord('A')
        counters[index] += 1

for i in range(N):
    code = i + ord('A')
    print(chr(code), counters[i])
