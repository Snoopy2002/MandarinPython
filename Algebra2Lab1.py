# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def listfunc(L):      
       s=0  
       for i in range(0,4):   
              s=s+L[i]
       print(s)

L= []  
for i in range (0,4):
       x=int(input("Enter a number: "))
       L.append(x)
listfunc(L)
