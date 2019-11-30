# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:33:42 2019

@author: Snoopy
"""
import random
import turtle
import math
from sys import platform
import datetime


global colors
colors=("green", "blue", "violet", "red", "orange", "yellow", "lightblue")

global maximum
maximum=500
global minimum
minimum=-500

global max2
max2=400
global min2
min2=-400

global sizeincrease
sizeincrease=60



def drawcircle(T):
     
    x=random.randint(min2,max2)
    y=random.randint(min2, max2)
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
    
    x=random.randint(min2, max2)
    y=random.randint(min2, max2)
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
    x=random.randint(min2, max2)
    y=random.randint(min2, max2)
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
    x=random.randint(min2, max2)
    y=random.randint(min2, max2)
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

def drawtrianglegeometrysss(T,w, fn): #draw SSS Triangle
    
    dist1=w.numinput("Make SSS triangle", "Enter the length of side 1")
    dist2=w.numinput("Make SSS triangle", "Enter the length of side 2")
    dist3=w.numinput("Make SSS triangle", "Enter the length of side 3")
    dist1a=w.numinput("Make SSS triangle", "Enter the length of side 1 of the 2nd triangle")
    dist1b=w.numinput("Make SSS triangle", "Enter the length of side 2 of the 2nd triangle")
    dist1c=w.numinput("Make SSS triangle", "Enter the length of side 3 of the 2nd triangle")
    
    if(dist1 is not None and dist2  is not None and dist3 is not None and dist1a is not None and dist1b is not None and dist1c is not None):
    
      if (dist1==dist1a and dist2==dist1b and dist3==dist1c): #draw the 2 SSS triangles
          dist1=dist1+sizeincrease
          dist2=dist2+sizeincrease
          dist3=dist3+sizeincrease
          x1=random.randint(minimum, maximum)
          y1=random.randint(minimum, maximum)
    
           
          T.goto(x1,y1)
          T.pendown()
          c=random.choice(colors)
          T.fillcolor(c)
          T.begin_fill()
          T.right(60)
          T.forward(dist1)
          T.right(120)
          T.forward(dist2)
          T.right(120)
          T.goto(x1,y1)
          T.end_fill()
          T.up()
          
          
          #draw the 2nd matching triangle
          dist1a=dist1a+sizeincrease
          dist1b=dist1b+sizeincrease
          dist1c=dist1c+sizeincrease
          T.goto(x1+80,y1)
          T.pendown()
          T.fillcolor(c)
          T.begin_fill()
          T.right(60)
          T.forward(dist1a)
          T.right(120)
          T.forward(dist1b)
          T.right(120)
          T.goto(x1+80,y1)
          T.end_fill()
          T.up()
          
          #write on screen
          T.up()
          T.color(c)
          T.goto(x1+100, y1-100)
          T.write('SSS Triangles', move=(0,0), font=("Arial", 30, "normal"))
          T.up()
          
          #write student info to file
          F=open(fn, 'a+')
          time=datetime.datetime.now()
          F.write(f"{time}\n")
          F.write(f"SSS Side lengths: {dist1}, {dist2}, {dist3}\n")
          F.write(f"SSS Angles: 60, 60, 60\n")
          print("Data written to file.")
          F.close()
      else:
        T.up()
        T.goto(0,450)
        T.pendown()
        c=random.choice(colors)
        T.color(c)
        T.begin_fill()
        T.write('No SSS triangle!', move=True, align="left", font=("Arial", 30, "normal"))
        T.up()
    
    return()
    
def drawtrianglegeometrysas(T,w, fn): #draw SAS triangles
    dist1=w.numinput("Make SAS triangle", "Enter the length of side 1" )
    angle2=w.numinput("Make SAS triangle", "Enter the included angle of the triangle")
    dist2=w.numinput("Make SAS triangle", "Enter the length of side 2" )
    
    dist1a=w.numinput("Make SAS triangle", "Enter the length of side 1 of the 2nd triangle" )
    dist2a=w.numinput("Make SAS triangle", "Enter the length of side 2 of the 2nd triangle" )
    if(dist1 is not  None and dist2 is not None and angle2 is not None and dist1a is not None and dist2a is not None):
      if (dist1==dist1a and angle2 <=178 and dist2==dist2a):
        dist1=dist1+sizeincrease
        dist2=dist2+sizeincrease
        angle1=(180-angle2)/2
        angle3=(180-angle2)/2
        x1=random.randint(minimum, maximum)
        y1=random.randint(minimum, maximum)
         #draw the two matching triangles 
        T.goto(x1,y1)
        T.pendown()
        c=random.choice(colors)
        T.fillcolor(c)
        T.begin_fill()
        T.right(180-angle3)
        T.forward(dist1)
        T.right(180-angle2)
        T.forward(dist2)
        T.right(180-angle1)
        loc=T.pos()
        valuex=loc[0]
        valuey=loc[1]
        dist3=math.sqrt((valuex-x1)**2+(valuey-y1)**2) #distance formula gives side 3
        T.goto(x1,y1)
        T.end_fill()
        T.up()
        
        T.goto(x1+100,y1) #draw the second matching triangle
        dist1a=dist1a+sizeincrease
        dist2a=dist2a+sizeincrease
        T.pendown()
        T.fillcolor(c)
        T.begin_fill()
        T.right(180-angle3)
        T.forward(dist1a)
        T.right(180-angle2)
        T.forward(dist2a)
        T.right(180-angle1)
        T.goto(x1+100,y1)
        T.end_fill()
        T.up()
        
        #write on screen
        T.up()
        T.color(c)
        T.goto(x1+50, y1-50)
        T.write('SAS Triangles', move=(0,0), font=("Arial", 30, "normal"))
        T.up()
        
        #write student info to file
        F=open(fn, 'a+')
        time=datetime.datetime.now()
        F.write(f"{time}\n")
        F.write(f"SAS Side lengths: {dist1}, {dist2}, {dist3}\n")
        F.write(f"SAS Angles: {angle1},{angle2},{angle3}\n")
        print("Data written to file")
        F.close()
        
      else:
        T.up()
        T.goto(-300, 250)
        T.pendown()
        c=random.choice(colors)
        T.color(c)        
        T.begin_fill()
        T.write('No SAS triangle!', move=True, align="left", font=("Arial", 30, "normal"))
        T.up()
    
    return()
    
    
def drawtrianglegeometryasa(T,w, fn): #draw ASA triangles
    angle1=w.numinput("Make ASA triangle", "Enter angle 1" )
    dist1=w.numinput("Make ASA triangle", "Enter the included side of the triangle")
    angle2=w.numinput("Make ASA triangle", "Enter the angle 2" )
    
    if(angle1 is not None and angle2 is not None and dist1 is not None):
    
      if (angle1+angle2 < 179):   
        dist1=dist1+sizeincrease
        dist2=dist1/2
        angle3=180-(angle1+angle2)
        x1=random.randint(minimum, maximum)
        y1=random.randint(minimum, maximum)
        T.goto(x1,y1)
        T.pendown()
        c=random.choice(colors)
        T.fillcolor(c)
        T.begin_fill()
        T.right(180-angle1)
        T.forward(dist1)
        T.right(180-angle2)
        T.forward(dist2)
        T.right(180-angle3)
        loc=T.pos()
        valuex=loc[0]
        valuey=loc[1]
        dist3=math.sqrt((valuex-x1)**2+(valuey-y1)**2) #distance formula gives side 3
        T.end_fill()
        T.up()
        
        T.color(c)  #draw the 2nd matching triangle
        T.goto(x1-100,y1-100)
        T.pendown()
        T.fillcolor(c)
        T.begin_fill()
        T.right(180-angle1)
        T.forward(dist1)
        T.right(180-angle2)
        T.forward(dist2)
        T.right(180-angle3)
        T.goto(x1-100,y1-100)
        T.end_fill()
        T.up()
        
        #write on screen
        T.color(c)
        T.goto(x1-50, y1-75)
        T.write('ASA Triangles', move=(0,0), font=("Arial", 30, "normal"))
        T.up()
    
        #write student info to file
        F=open(fn, 'a+')
        time=datetime.datetime.now()
        F.write(f"{time}\n")
        F.write(f"ASA Side lengths: {dist1}, {dist2}, {dist3}\n")
        F.write(f"ASA Angles: {angle1},{angle2}, {angle3}\n")
        print("Data written to file")
        F.close()
        
      else:
        T.up()
        T.goto(-300,-300)
        T.pendown()
        c=random.choice(colors)
        T.color(c)
        T.begin_fill()
        T.write('No ASA triangle!', move=True, align="left", font=("Arial", 30, "normal"))
        T.up()
    
    return()
    
    
def drawtrianglegeometryaas(T,w, fn): #draw AAS triangles
    angle1=w.numinput("Make AAS triangle", "Enter angle 1" )
    dist2=w.numinput("Make AAS triangle", "Enter the nonincluded side of the triangle")
    angle2=w.numinput("Make AAS triangle", "Enter the angle 2" )
    
    if(angle1 != None and angle2 != None and dist2 != None):
    
      if (angle1+angle2 < 179):   
        dist1=random.randint(20,80)
        angle3=180-(angle1+angle2)
        x1=random.randint(minimum, maximum)
        y1=random.randint(minimum, maximum)
        T.goto(x1,y1)
        T.pendown()
        c=random.choice(colors)
        T.fillcolor(c)
        T.begin_fill()
        T.right(180-angle1)
        T.forward(dist1)
        T.right(180-angle2)
        T.forward(dist2)
        T.right(180-angle3)
        loc=T.pos()
        valuex=loc[0]
        valuey=loc[1]
        dist3=math.sqrt((valuex-x1)**2+(valuey-y1)**2) #distance formula gives side 3
        T.end_fill()
        T.up()
        
        T.color(c)  #draw the 2nd matching triangle
        T.goto(x1-100,y1-100)
        T.pendown()
        T.fillcolor(c)
        T.begin_fill()
        T.right(180-angle1)
        T.forward(dist1)
        T.right(180-angle2)
        T.forward(dist2)
        T.right(180-angle3)
        T.goto(x1-100,y1-100)
        T.end_fill()
        T.up()
        
        #write on screen
        T.color(c)
        T.goto(x1-75,y1-75)
        T.write('AAS Triangles', move=(0,0), font=("Arial", 30, "normal"))
        T.up()
        
        #write student info to file
        F=open(fn, 'a+')
        time=datetime.datetime.now()
        F.write(f"{time}\n")
        F.write(f"AAS Side lengths: {dist1}, {dist2}, {dist3}\n")
        F.write(f"AAS Angles: {angle1}, {angle2}, {angle3}\n")
        print("Data written to file.")
        F.close()
        
      else:
        T.up()
        T.goto(-400,250)
        T.pendown()
        c=random.choice(colors)
        T.color(c)
        T.begin_fill()
        T.write('No AAS triangle!', move=True, align="left", font=("Arial", 30, "normal"))
        T.up()
    
    return()
    
if __name__ == "__main__":
    
    
      random.seed()
      name=input("Enter your name: ")
      filename=name+".txt"
      choice=input("Do you want to work with triangles? (y/n)")
      if choice == 'Y' or choice=='y':
          
          try: #code needed to prevent crash every other run of program
             tina=turtle.Turtle()
             wn=turtle.Screen()
             wn.setup(width=800,height=800)
             wn.bgcolor("black")
             wn.title("Turtle Drawing Window: Press x to close.")
             tina.shape("turtle") #makes cursor a turtle
             tina.resizemode("user") #allows change of turtle size in next line
             tina.shapesize(1,1,1) #resize turtle
             drawtrianglegeometrysss(tina, wn, filename)
             drawtrianglegeometrysas(tina,wn, filename)
             drawtrianglegeometryasa(tina,wn, filename)
             drawtrianglegeometryaas(tina,wn, filename)
             if platform=="win32":
               wn.exitonclick()
          except:
             tina=turtle.Turtle()
             wn=turtle.Screen()
             wn.setup(width=800,height=800)
             wn.bgcolor("black")
             wn.title("Turtle Drawing Window: Press x to close.")
             tina.shape("turtle") #makes cursor a turtle
             tina.resizemode("user") #allows change of turtle size in next line
             tina.shapesize(1,1,1) #resize turtle
             drawtrianglegeometrysss(tina, wn, filename)
             drawtrianglegeometrysas(tina, wn, filename)
             drawtrianglegeometryasa(tina,wn, filename)
             drawtrianglegeometryaas(tina,wn, filename)
             if platform=="win32":
               wn.exitonclick()
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
             #tina.stamp()
             x+=1
          tina.home()
          tina.pendown()
          c=random.choice(colors)
          tina.color(c)
          tina.begin_fill()
          tina.write('Hope you enjoyed the show.', move=True, align="left", font=("Arial", 20, "normal"))
          if platform=="win32":
             wn.exitonclick()
          
