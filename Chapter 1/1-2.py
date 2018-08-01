#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:16:54 2018

@author: snoopy
"""

#simple program to introduce creates a multiplication table

def mtable(n,t):
    for k in range(0,11):
        c=n*k
        print(n, "*", k, "=", c, "\n")

if __name__ == '__main__':
    n=input("Enter a number whose times table you want to display: ")
    n=int(n)
    t=input("Enter the number of multiples you want: ")
    t=int(t)
    mtable(n,t)
    
        