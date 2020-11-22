#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import random

FIRST = ord('A')
rows = cols = size = 1

while size % 2 != 0:
    rows = int(input('Rows? '))
    cols = int(input('Cols? '))
    size = rows * cols

matrix = [chr(FIRST + i // 2) for i in range(size)]

for i in range(size):
    print(matrix[i], end='')
    if i % cols == cols - 1:
        print()
print()

random.shuffle(matrix)
## for i in range(size):
##     j = random.randrange(size)
##     matrix[i], matrix[j] = matrix[j], matrix[i]

for i in range(size):
    print(matrix[i], end='')
    if i % cols == cols - 1:
        print()

