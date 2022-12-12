"""
ITS 1801 F22
Project 01 Solution
"""

import turtle
from readchar import readkey, key

t = turtle.Turtle()
t.shape("turtle")

# While loops runs forever and every time it runs reads a key from
# the keyboard
while True:
  k = readkey();
  # Move backward
  if k == "a":
    t.backward(5)
  # Move forwared
  elif k == "d":
    t.forward(5)
  # Rotate left two degrees
  elif k == "r":
    t.left(2)
  # Rotate left five degrees
  elif k == "f":
    t.left(5)
  # Pen up
  elif k == "u":
    t.penup()
  # Pen down
  elif k == "i":
    t.pendown()
    
 
