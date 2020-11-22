#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

x, y, dx, count = 50, 50, 5, 0
ARENA_W, ARENA_H, MARGIN = 480, 360, 100
image = g2d.load_image("ball.png")

def tick():
    global x, dx, count
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))
    if g2d.key_pressed("LeftButton"):
        count = 5
    if count > 0:
        count -= 1
        if x + dx < -MARGIN:
            x = ARENA_W + MARGIN
        if x + dx > ARENA_W + MARGIN:
            x = -MARGIN
        x += dx

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick, 5)  # call tick 5 times/second

main()
