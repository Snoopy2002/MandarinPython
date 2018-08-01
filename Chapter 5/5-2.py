#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#die roll simulator and the law of large numbers Saha 5-2

import random

def dieroll():
    return random.randint(1,6)
    
    
numrolls = 0
sumA=0
sumB=0
sumC=0
sumD=0
sumE=0

print("Expected average  value 3.5")
while numrolls < 100:
    roll=dieroll()
    sumA += roll
    numrolls += 1
avgA=sumA/100

numrolls=0
while numrolls < 1000:
    roll=dieroll()
    sumB += roll
    numrolls += 1
avgB=sumB/1000

numrolls=0    
while numrolls < 10000:
    roll=dieroll()
    sumC += roll
    numrolls += 1
avgC=sumC/10000

numrolls=0
while numrolls < 100000:
    roll=dieroll()
    sumD += roll
    numrolls += 1
avgD=sumD/100000

numrolls=0    
while numrolls < 500000:
    roll=dieroll()
    sumE += roll
    numrolls += 1
avgE=sumE/500000

print("Trials: 100          Trial Average:", avgA)
print("Trials: 1000          Trial Average:", avgB)
print("Trials: 10000         Trial Average:", avgC)
print("Trials: 100000          Trial Average:", avgD)
print("Trials: 500000          Trial Average:", avgE)

