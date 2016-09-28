
import sys
import os
import math
import copy

class Point(object):
    """Represent point in 2-D space"""


class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """

def print_point(p):
    print '(%g, %g)' % (p.x, p.y)

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    return rect

def deep_move_rect(rect, dx, dy):
    new_rect = copy.deepcopy(rect)
    rect.corner.x += dx
    rect.corner.y += dy
    print "Is rect == to new_rect:", rect is new_rect 
    return rect


def main():
    
    my_rect = Rectangle()

    my_rect.corner = Point()
    my_rect.width = 10.0
    my_rect.height = 20.0

    my_rect.corner.x = 15
    my_rect.corner.y = 10
    print_point(my_rect.corner)

    moved_rect = deep_move_rect(my_rect, 5, 8)
    print_point(moved_rect.corner)


if __name__ == '__main__':
    main()
