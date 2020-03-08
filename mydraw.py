# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:37:32 2020

@author: danhhong
"""

import turtle

# draw star shape
def DrawStar():
    turtle.pensize(5)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    
    while True:
        turtle.forward(300)
        turtle.right(144)
        if abs(turtle.pos()) < 1:
            break
    
    turtle.end_fill()
    
    turtle.hideturtle()
    turtle.done()

# draw sun rising shape
def DrawSun():
    turtle.pensize(2)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    
    while True:
        turtle.forward(300)
        turtle.right(170)
        if abs(turtle.pos()) < 1:
            break
    
    turtle.end_fill()
    
    turtle.hideturtle()
    turtle.done()

# draw square shape
def DrawSquare():
    turtle.pensize(5)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
        
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()

