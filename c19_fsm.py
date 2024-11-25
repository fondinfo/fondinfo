#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

alphabet = {"a", "b"}
states = {"Q0", "Q1", "Q2", "Q3"}
start = "Q0"
accepting = {"Q0"}
transition = {("Q0", "a"): "Q1", ("Q0", "b"): "Q2",
              ("Q1", "a"): "Q0", ("Q1", "b"): "Q3",
              ("Q2", "a"): "Q3", ("Q2", "b"): "Q0",
              ("Q3", "a"): "Q2", ("Q3", "b"): "Q1"}

def compute(string: str) -> bool:
    state = start
    for symbol in string:
        if symbol not in alphabet:
            raise ValueError(symbol + "∉Σ, Σ=" + str(alphabet))

        new_state = transition.get((state, symbol), None)
        print((state, symbol), "→", new_state)
        state = new_state
        if not state:
            return False  # implicit error trap state
        
    return state in accepting

if __name__ == "__main__":
    string = input("String? ")  # ababaabb
    result = compute(string)
    print("Result:", result)
