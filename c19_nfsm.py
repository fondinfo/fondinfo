#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

alphabet = {"a", "b"}
all_states = {"Q0", "Q1"}
start = "Q0"
accepting = {"Q1"}
transition = {("Q0", "a"): {"Q0"},
              ("Q0", "b"): {"Q0", "Q1"}}

def compute(string: str) -> bool:
    states = {start}
    for symbol in string:
        if symbol not in alphabet:
            raise ValueError(symbol + "∉Σ, Σ=" + str(alphabet))

        new_states = set()
        for state in states:
            new_states |= transition.get((state, symbol), set())  # union
        print((states, symbol), "→", new_states)
        states = new_states
        if not states:
            return False
        
    return states & accepting != set()

if __name__ == "__main__":
    string = input("String? ")  # abaab
    result = compute(string)
    print("Result:", result)
