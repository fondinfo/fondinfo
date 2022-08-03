#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d, p03_pen
import math

def draw_tree(pos, length, angle):
    nxt = p03_pen.next_pos(pos, length, angle)
    if length < 5:
        g2d.set_color((0, 255, 0))
        g2d.draw_line(pos, nxt)
    else:
        g2d.set_color((128, 64, 0))
        g2d.draw_line(pos, nxt)
        draw_tree(nxt, length * 4 / 5, angle + math.pi / 6)
        draw_tree(nxt, length * 4 / 5, angle - math.pi / 6)

def main():
    g2d.init_canvas((600, 600))
    draw_tree((300, 600), 80, -math.pi / 2)
    g2d.main_loop()

main()
