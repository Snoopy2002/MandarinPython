# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:18:16 2019

@author: Snoopy
"""



import turtle
from sys import platform
import time


global colors
colors=("green", "blue", "violet", "red", "orange", "yellow", "lightblue")

global maximum
maximum=300
global minimum
minimum=-300


def dragging(x,y):
     T.ondrag(None)
     T.setheading(T.towards(x, y))
     T.goto(x, y)
     loc=T.pos()
     print(loc[0], loc[1]) #prints the turtle location to the console
     if loc[0] > maximum or loc[0] < minimum or loc[1] > maximum or loc[1] < minimum:
         T.up()
         T.home()
         clearval=screen.numinput("Clear Screen","Enter 1 to clear screen: ", 0 )
         if clearval == 1:
             T.clear()
             
     T.ondrag(dragging)
     
def down(x,y):
    T.down()
    T.ondrag(dragging)
   
def exercise2(T):
    T.shape("turtle") #makes cursor a turtle
    T.color("blue")
    T.resizemode("user") #allows change of turtle size in next line
    T.shapesize(2,2,2) #resize turtle
    T.speed(3)
    T.up()
    T.setpos(50,100)
    T.down()
    T.begin_fill()
    T.color("yellow")
    T.fillcolor("yellow")
    for c in range(4):
        T.forward(60)
        T.right(90)
    T.end_fill()
    T.up()
    T.setpos(-150,50)
    T.color("green")
    T.fillcolor("green")
    T.down()
    T.begin_fill()
    for c in range(4):
        T.forward(70)
        T.right(90)
    T.end_fill()
    T.up()
    T.setpos(-150,-90)
    T.color("red")
    T.fillcolor("red")
    T.down()
    T.begin_fill()
    for c in range(4):
        T.forward(100)
        T.right(90)
    T.end_fill()
    T.up()
    T.setpos(150,-90)
    T.color("blue")
    T.fillcolor("blue")
    T.down()
    T.begin_fill()
    for c in range(4):
        T.forward(100)
        T.right(90)
    T.end_fill()
    return()
    
def Exercise3drawTandP(wn,T):
    T.up()
    T.setpos(-250,-100)
    T.down()
    T.begin_fill()
    T.color("violet")
    T.fillcolor("violet")
    T.setheading(0)
    for c in range(3):
        T.forward(60)
        T.right(120)
    T.end_fill()
    T.up()
    T.setpos(250,-100)
    T.down()
    #T.begin_fill()
    T.color("red")
    T.fillcolor("red")
    T.setheading(0)
    T.begin_poly()
    for c in range(5):
        T.forward(60)
        T.right(72)
    T.end_poly()
    for i in range(3):
        exercise4movepentagon(wn,T)
    #T.end_fill()
    return()
    
def exercise4movepentagon(wn,T):
    locs=T.get_poly()
    print(locs)
    #move the pentagon n units on x and y according to user
    movex=wn.numinput("How many units to move x: ", "Enter a value" )
    movey=wn.numinput("How many units to move y: ", "Enter a value")
    T.up()
    T.setpos(locs[0][0]+movex,locs[0][1]+movey)
    T.down()
    T.begin_poly()
    for c in range(5):
        T.forward(60)
        T.right(72)
    T.end_poly()
    locs=T.get_poly()
    #print(locs)
                  
    '''
       #spin the pentagon
    shape=turtle.Shape("polygon", T.get_poly())
    #shape.addcomponent(T.get_poly(), "blue")
    wn.register_shape("pentagon",shape)
    T.shape("pentagon")
    T.up()
    T.setpos(0,0)
    T.down()
    start=time.time()
    while(time.time() - start < 8):
        for theta in range(0, 360, 10):
            T.setheading(-theta)         
    if platform=="win32":
       wn.exitonclick()
       '''
        
    
def exercise3(wn,T): #draws rectangle and square
    #wn=turtle.Screen()
    #wn.screensize(maximum, minimum,"black")
    #wn.title("Turtle Drawing Window: Press x to close.")
    T.shape("turtle") #makes cursor a turtle
    T.color("blue")
    T.resizemode("user") #allows change of turtle size in next line
    T.shapesize(1,1,1) #resize turtle
    T.speed(8)
    T.up()
    T.setpos(50,100)
    T.down()
    T.begin_fill()
    T.color("yellow")
    T.fillcolor("yellow")
    for c in range(4):
        T.forward(60)
        T.right(90)
    T.end_fill()
    T.up()
    T.setpos(-150,50)
    T.color("green")
    T.fillcolor("green")
    T.down()
    T.begin_fill()
    T.forward(90)
    T.right(90)
    T.forward(50)
    T.right(90)
    T.forward(90)
    T.right(90)
    T.forward(50)    
    T.end_fill()
    Exercise3drawTandP(wn,T)
    return()
    
    
    
def drawithturtle(T):
    T.shape("turtle") #makes cursor a turtle
    T.color("blue")
    T.resizemode("user") #allows change of turtle size in next line
    T.shapesize(1,1,1) #resize turtle
    T.fillcolor("blue")
    T.begin_fill()
    T.forward(100)
    T.right(90)
    T.forward(100)
    T.right(90)
    T.forward(100)
    T.right(90)
    T.forward(100)
    T.up()
    T.setpos(-100,-100)
    T.end_fill()
    T.down()
    T.fillcolor("green")
    T.begin_fill()
    for i in range(4):
        T.forward(50)
        T.right(90)
    T.end_fill()
    #if platform=="win32":
       #wn.exitonclick()
      
    return()
    
def drawsquare(T):
    T.down()
    T.begin_fill()
    T.color("yellow")
    T.fillcolor("yellow")
    T.begin_poly()
    for c in range(4):
        T.forward(60)
        T.right(90)
    T.end_fill() 
    T.end_poly()
    T.up()
    locations=T.get_poly()
    print(locations)


if __name__ == "__main__":
    
          try: #code needed to prevent crash every other run of program
             T=turtle.Turtle()
             T.speed(3)
             screen = turtle.Screen() 
             screen.screensize(maximum, minimum, "black")
             screen.title("Turtle Drawing Window: Press x to close.")
             T.shape("turtle")             
             #drawithturtle(T)
             #exercise2(T) 
             exercise3(screen,T)
             #below code handles free draw with turtle
             #drawsquare(T)
             T.ondrag(dragging)
             T.onclick(down)                        
             screen.listen()             
             screen.mainloop()
          except:
             T=turtle.Turtle()
             T.speed(3)
             screen = turtle.Screen() 
             screen.screensize(maximum, minimum, "black")
             screen.title("Turtle Drawing Window: Press x to close.")
             T.shape("turtle")
             #drawithturtle(T)
             #exercise2(T)
             exercise3(screen,T)
             #drawsquare(T)
             #below code allows free draw with turtle
             T.ondrag(dragging)
             T.onclick(down)    
             screen.listen()
             screen.mainloop()
     
          
    