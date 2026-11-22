#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from c12_stack import Stack
from typing import Iterable
from operator import add, sub, mul, truediv, neg

BINARY = {"+": add, "-": sub, "*": mul, "/": truediv}
UNARY = {"~": neg}

def evaluate(tokens: Iterable[str]) -> float:
    s = Stack()
    for token in tokens:
        if token in BINARY:
            b = s.pop()
            a = s.pop()
            s.push(BINARY[token](a, b))
        elif token in UNARY:
            s.push(UNARY[token](s.pop()))
        else:
            s.push(float(token))
    return s.pop()

def main():
    expr = "4 2 3 * + 5 *".split()
    v = evaluate(iter(expr))
    print(v)

if __name__ == "__main__":
    main()
