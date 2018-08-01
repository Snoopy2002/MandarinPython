#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 03:43:09 2017

@author: snoopy
"""

from fractions import Fraction

def add(a,b):
    print("Result of Addition: {0}".format(a+b))
    
def subtract(a,b):
    print("Result of Subtraction: {0}".format(a-b))

def multiply(a,b):
    print("Result of Multiplication: {0}".format(a*b))
    
def divide(a,b):
    print("Result of Division 1: {0}".format(a/b))
    
    
if __name__ == '__main__':
  choice = 'y'
  while(choice == 'y'):
    a=input("Enter the first fraction: ")
    b=input("Enter the second fraction: ")
    try:
      a=Fraction(a)
      b=Fraction(b)
    except:
      print("You entered the fraction incorrectly.")
    else:
      op=input("Enter the operation to perform (A for Add, M for Multiply, S for Subtract, D for divide: ")
      if op == 'A':
          add(a,b)
      elif op == 'S':
          subtract(a,b)
      elif op == 'M':
          multiply(a,b)
      else:
          divide(a,b)
    choice = input("Another? (y/n) ")
    
        
        
        
    