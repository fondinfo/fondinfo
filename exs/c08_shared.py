#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

text1 = "some bla bla stuff and then more bla bla stuff"
text2 = "also the same bla bla stuff over and over"

words1 = text1.split(" ")
words2 = text2.split(" ")

shared = set(words1) & set(words2)  # intersection

for w in shared:
    print(w)
