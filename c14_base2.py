#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def to_bits(n: int) -> str:
    bits = ""
    while n != 0:
        bit = n % 2
        n = n // 2
        bits = str(bit) + bits
    return max(bits, "0")  # "0" instead of ""

def from_bits(bits: str) -> int:
    n = 0
    bitval = 1
    for bit in reversed(bits):
        n += int(bit) * bitval
        bitval *= 2
    return n

def main():
    n = int(input("n? "))
    bits = to_bits(n)
    print(bits, "=", from_bits(bits))

if __name__ == "__main__":
    main()