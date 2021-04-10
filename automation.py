"""
Get the location of the mirror software on the screen
"""
import pyautogui as gui
from pyautogui import Point
import time

# input('Move to top left of the mirror software and press enter')
# left = gui.position()
# input('Move to bottom right of the mirror software and press enter')
# right = gui.position()
# print("Location: [{}, {}, {}, {}]".format(left.x, left.y, right.x, right.y))
# exit()

location = [16, 193, 2173, 1810]
left = Point(location[0], location[1])
right = Point(location[2], location[3])
delay = 20


def hold(x, y):
    """
    Hold left mouse
    """
    gui.moveTo(x, y)
    gui.mouseDown(duration=delay)


def slide(x1, y1, x2, y2):
    """
    Slide from (x1, y1) to (x2, y2)
    """
    gui.mouseDown(x1, y1)
    gui.moveTo(x2, y2)
    release()


def release():
    """
    lift the left key
    """
    gui.mouseUp()


def get_bottom_center(left, right):
    """
    Get bottom center on the screen
    """
    x = (right.x - left.x) / 2 + left.x
    y = right.y - (right.y - left.y) / 5
    return (x, y)


def get_bottom_right(left, right):
    """
    Get bottom right on the screen
    """
    x = right.x - (right.x - left.x) / 8
    y = right.y - (right.y - left.y) / 8
    return (x, y)


screen_scale = 1
(px, py) = gui.position()
(x, y) = get_bottom_center(left, right)
(sx, sy) = get_bottom_right(left, right)

# focus the game
gui.mouseDown(x, y)
while True:
    # start the game
    # handle end game
    for i in range(5):
        slide(sx, sy, sx, sy - 200)

    time.sleep(5)
    # handle end game
    for i in range(5):
        slide(sx, sy, sx, sy - 200)

    hold(x, y)
    time.sleep(delay)

    time.sleep(5)
