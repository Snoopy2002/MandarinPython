#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Circle Area Simulator via Monte Carlo methods

import random
import math

def xandy():
    x=random.uniform(0,2*r)
    y=random.uniform(0,2*r)
    return(x,y)
    
def dartthrow(x1,y1,r):
    if(math.sqrt((x1*x1)+(y1*y1)) <= r):
        locincircle=1
    else:
        locincircle=0
    return locincircle

random.seed()   
est=1
while(est == 1):
    r=input("Enter the radius of the circle: ")
    r=float(r)
    C=input("Enter the number of dart-throws to the square: ")
    C=int(C)
    N=0
    M=0
    for k in range(C):
        x,y=xandy()
        loc=dartthrow(x,y,r)
        if (loc == 1):
            N=N+1
        else:
            M=M+1
    frac=1-N/(N+M) #fraction that land in the circle
    #print(frac)
    Aest=frac*4*r*r #estimated area of the circle
    #print("Radius: ", r)
    print("Area of the circle: ", math.pi*r*r, " Estimated Area with ", C, " darts is: ", Aest)
    PIest=4*frac
    print("Estimate of Pi is: ", PIest)
    est=input("Another circle? 1 to continue, any other # to quit: ")
    est=int(est)


        
        
