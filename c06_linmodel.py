#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

class LinearModel:
    def __init__(self, slope: float, intercept: float):
        self._a = slope
        self._b = intercept

    def predict(self, x: float) -> float:
        return self._a * x + self._b

def main():
    slope = float(input("Slope? "))
    intercept = float(input("Intercept? "))
    model = LinearModel(slope, intercept)

    line = input("x? ")
    while line != "":
        x = float(line)
        y = model.predict(x)
        print("y:", y)
        line = input("x? ")

if __name__ == "__main__":
    main()
