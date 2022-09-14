# CSCI 1100 Gateway to Computer Science
#
# This program demonstrates some simple animation/graphics routines.
#
# Covered: Wednesday September 14, 2022

# run: python3 introGraphics.py

from animate import *

# draw : unit -> image
#
def draw(ignored):
    backing = Image.rectangle(800, 800, Color.make(127, 0, 255))
    circle  = Image.circle(400, Color.White)
    return Image.placeImage(circle, (0, 0), backing)

# finished : unit -> boolean
#
def finished(ignored):
    return False

Animate.start(view=draw, stopWhen=finished)





