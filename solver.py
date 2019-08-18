# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 and Sun Aug 18 2019

@author: Snoopy
"""

#quadratic, cubic, and quartic equation solver

import cmath
import sympy as sp
import random
import time


global TOL #error tolerance of root guess to terminate Newton's Method
TOL = 0.0001

colors=["red", "blue", "green", "violet", "orange", "brown"]



def quad(expr2): #quadratic formula
    c=expr2.all_coeffs()
    x1=(-c[1]+cmath.sqrt(c[1]**2-4*c[0]*c[2]))/(2*c[0])
    x2=(-c[1]-cmath.sqrt(c[1]**2-4*c[0]*c[2]))/(2*c[0])  
    return(x1,x2)
    

def cubicandquartic(expr1,x): #Newton's Method for finding real roots
    try:
       plt= sp.plot(expr1, xlim=(-5,5), ylim=(-40,40), adaptive=False, nb_of_points=100, legend=True, show=False)
       plt[0].line_color=random.choice(colors)
       plt.show()
    except:
       print("Error drawing graph!!!")
    else:
        time.sleep(4) #give time to draw the graph
        roots=[]
        f1=sp.diff(expr1,x) #take derivative for Newton's Method
        f0=eval(expr1) #convert the input expression to a Python function for application of Newton's method and use of subs to evaluate
        totalroots=int(input("Enter the apparent number of real roots from the graph: "))
        for i in range(totalroots): #application n times of Newton's Method for est. number of real roots
           guess=input("Enter the initial guess for the root, it should be greater than the actual root: ")
           guess=float(guess)
           steps=100
           guess2=guess-f0.subs(x,guess)/f1.subs(x,guess)
           count=0
        while count < steps and abs(guess2-guess)>TOL: #keep computing until desired tolerance or iterations reached
           guess=guess2
           guess2=guess-f0.subs(x,guess)/f1.subs(x,guess)
           count += 1
           roots.append(sp.N(guess2,5))
        return(roots)
    
    

if __name__ == "__main__":

   expr1=input('Enter the polynomial:  ')
   sym=input('Enter the variable letter: ')

   try:
      exprS=sp.sympify(expr1)
        
   except:
      print("invalid function input try again" )
    
   else:
      x=sp.Symbol(sym)
      value=input("Enter the degree of the polynomial, (2 for quadratic, any other whole number for higher): ")
      if value == '2':
         plt= sp.plot(expr1, xlim=(-10,10), ylim=(-100,100), adaptive=False, nb_of_points=400, legend=True)
         plt[0].line_color=random.choice(colors)
         plt.show()
         exprS=sp.Poly(expr1)
         roots1,roots2=quad(exprS)
         print(f"{expr1} has roots of {roots1} , {roots2}")
         
      elif int(value) > 2:
         roots=cubicandquartic(expr1,x)
         sp.pprint(expr1)
         print(f"{expr1} has roots of {roots}")
       
    
    
    