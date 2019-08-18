# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:25:48 2019

@author: FruzzettiG
"""

from turtle import Turtle, Screen, Shape

screen = Screen()
screen.bgcolor('SkyBlue')

shape = Shape('compound')

turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.penup()

turtle.goto(-100, 0)

turtle.begin_poly()
turtle.goto(-100, 50)
turtle.goto(100, 50)
turtle.goto(100, 0)
turtle.goto(-100, 0)
turtle.end_poly()
shape.addcomponent(turtle.get_poly(), 'red')

turtle.goto(-100, 50)

turtle.begin_poly()
turtle.goto(0, 100)
turtle.goto(100, 50)
turtle.goto(-100, 50)
turtle.end_poly()
shape.addcomponent(turtle.get_poly(), 'brown')

turtle.goto(-40, 0)

turtle.begin_poly()
turtle.goto(-40, 30)
turtle.goto(-20, 30)
turtle.goto(-20, 0)
turtle.goto(-40, 0)
turtle.end_poly()
shape.addcomponent(turtle.get_poly(), 'orange')

turtle.goto(20, 20)

turtle.begin_poly()
turtle.goto(20, 40)
turtle.goto(50, 40)
turtle.goto(50, 20)
turtle.goto(20, 20)
turtle.end_poly()
shape.addcomponent(turtle.get_poly(), 'white')

screen.register_shape('house', shape)

turtle.reset()
turtle.penup()

# Now we can move our house in any manner that we move a turtle:

turtle.shape('house')

for theta in range(0, 360, 10):
    turtle.setheading(theta)

turtle.setheading(90)
turtle.shearfactor(0.5)
turtle.goto(300, 300)
turtle.shearfactor(0)

screen.mainloop()