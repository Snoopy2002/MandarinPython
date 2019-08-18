# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:33:42 2019

@author: Snoopy
"""

global colors
colors=("green", "blue", "violet", "red", "orange", "yellow", "lightblue")

global maximum
maximum=350
global minimum
minimum=-350

import random
import turtle
import math
from sys import platform

def drawcircle(T):
     
    x=random.randint(minimum, maximum)
    y=random.randint(minimum, maximum)
    r=random.randint(5,20)
    T.up()
    T.setpos(x+r, y)
    T.down()
    c=random.choice(colors)
    T.fillcolor(c)
    T.begin_fill()
    for i in range(0,365,5):
         a=math.radians(i)
         T.setpos(x+r*math.cos(a), y+r*math.sin(a))
    T.end_fill()
    T.up()
    
    return()
   
    
def drawsquare(T):
    
    x=random.randint(minimum, maximum)
    y=random.randint(minimum, maximum)
    dist=random.randint(20,50)
    T.goto(x,y)
    T.down()
    T.setheading(0)
    c=random.choice(colors)
    T.fillcolor(c)
    T.begin_fill()
    x=0
    while(x < 4):
      T.forward(dist)
      T.right(90)
      x+=1
    T.end_fill()
    T.up()
    
    return()

def drawtriangle(T):
    x=random.randint(minimum, maximum)
    y=random.randint(minimum, maximum)
    dist=random.randint(20,50)
    T.goto(x,y)
    T.pendown()
    c=random.choice(colors)
    T.fillcolor(c)
    T.begin_fill()
    T.right(60)
    T.forward(dist)
    T.right(120)
    T.forward(dist)
    T.right(120)
    T.forward(dist)
    T.end_fill()
    T.up()
    
    return()
    
    
def drawhexagon(T):
    x=random.randint(minimum, maximum)
    y=random.randint(minimum, maximum)
    dist=random.randint(20,50)
    T.goto(x,y)
    T.pendown()
    c=random.choice(colors)
    T.fillcolor(c)
    T.begin_fill()
    x=0
    while(x<6):
      T.left(60)
      T.forward(dist)
      x+=1
    T.end_fill()
    T.up()
    return()
    
if __name__ == "__main__":
    
    
      random.seed()
      choice=input("Do you want to draw with turtle? (y/n)")
      if choice == 'Y' or choice=='y':
          
          try: #code needed to prevent crash every other run of program
             tina=turtle.Turtle()
             drawithturtle(tina)
          except:
             tina=turtle.Turtle()
             drawithturtle(tina)
      else:
          try: #prevents crash every other run of program
             tina=turtle.Turtle()
          except:
             tina=turtle.Turtle()
          wn=turtle.Screen()
          wn.setup(width=800,height=800)
          wn.bgcolor("black")
          wn.title("Turtle Drawing Window: Press x to close.")
          tina.shape("turtle") #makes cursor a turtle
          tina.resizemode("user") #allows change of turtle size in next line
          tina.shapesize(1,1,1) #resize turtle
          loopctr=random.randint(10,30)
          x=0
          funcs=[drawcircle, drawhexagon, drawsquare, drawtriangle]
          while(x<loopctr):
             random.choice(funcs)(tina)
             tina.stamp()
             x+=1
          tina.home()
          if platform=="win32":
             wn.exitonclick()
          
