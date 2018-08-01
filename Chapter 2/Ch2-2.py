#Quadratic Function Calculator and Plotter
"""
Created on Tue Oct 18 23:44:14 2016
Chapter 2 # 1 plotting temperature data
@author: snoopy
"""

import matplotlib.pyplot as plt
import pylab as plb
import sympy as sp
from sympy.abc import x

def Draw(xnums,ynums):
    plt.plot(xnums, ynums, color='darkblue', marker = '+', label='F(x)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(fontsize='small')
    plt.show()
    
expr1=input('Enter the first quadratic polynomial as x**n + x*p + q:  ')

try:
    F=sp.sympify(expr1)
except:
    print("invalid function input try again" )
    
print(expr1)    
xvals=[]
yvals=[]
xmin=input("Enter the minimum x-value: ")
xmax=input("Enter the maximum x-value: ")
xmin=int(xmin)
xmax=int(xmax)
for i in range(xmin, xmax): #set up the lists of data points for the function
    xvals.append(i)
    y=F.subs(x,i)
    yvals.append(y)
    
print(xvals, yvals)
Draw(xvals, yvals)

    

    


    

