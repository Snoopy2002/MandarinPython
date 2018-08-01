#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 23:44:14 2016
Chapter 2 # 1 plotting temperature data
@author: snoopy
"""

import matplotlib.pyplot as plt
import pylab as plb

def FtoC(f):
    C=(5/9)*(f-32)
    return(C)
     
i=0
k=0
Rhigh=[]
Rlow=[]
RChigh=[]
RClow=[]

for i in range (12):
         h=input("Enter a monthly average high in F : ")
         l=input("Enter a monthly average low in F: ")
         h=int(h)
         l=int(l)
         Rhigh.append(h)
         Rlow.append(l)         
     
for k in range (12):
      F=Rhigh[k]
      C=FtoC(F)
      C=round(C,3)
      RChigh.append(C)
      F=Rlow[k]
      C=FtoC(F)
      C=round(C,3)
      RClow.append(C)
      
print("Highs and Lows in Degrees C") 
print(RChigh, RClow)      
     
months=[1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(months, Rhigh, months, Rlow, marker='o')
plt.xlabel("Month")
plt.ylabel("Temp in F")
plt.title("Average Hign and Low Temps in Raleigh")
plb.legend(["Highs", "Lows"])
plt.show()