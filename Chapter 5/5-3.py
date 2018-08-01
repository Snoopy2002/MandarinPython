#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Coin toss simulator Saha 5-3

import random

def cointoss():
    return random.randint(0,1)
    
avcash=input("Enter your starting amount of money: ")
avcash=float(avcash)
counter=0
print("Expected average  value 3.5")
while avcash > 0:
    counter=counter+1
    toss=cointoss()
    if(toss==0):
        avcash += 1.00
        print("Heads!     Current Amount: $" , avcash)
    else:
        avcash -= 1.50
        print("Tails!     Current Amount: $"  , avcash)
print("Game ended, coin tosses: ", counter)
    

