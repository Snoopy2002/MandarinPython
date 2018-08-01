#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:42:46 2017

@author: snoopy
"""

#P19: Unit conversion

'''
Unit converter: Miles and Kilometers
'''
def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to lb')
    print('4. Lb to Kilograms')
    print('5. C to F')
    print('6. F to C')
    
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))
    
def kgtolb():
    kg = input('Enter the weight in kilograms: ')
    kg = float(kg)
    lb = 2.2*kg
    print('Weight in lb: {0}'.format(lb))
    
def lbtokg():
    lb = input('Enter the weight in pounds: ')
    lb = float(lb)
    kg = lb/2.2
    print('Weight in kg: {0}'.format(kg))
    
def CtoF():
    C = input('Enter the temperature in C: ')
    C = float(C)
    F = (9/5)*C+32
    print('Temp in F: {0}'.format(F))
    
def FtoC():
    F = input('Enter the temp in F: ')
    F = float(F)
    C = (5/9)*(F-32)
    print('Temp in C: {0}'.format(C))
    

    

if __name__ == '__main__':
    choice = 'y'
    while(choice == 'y'):
      print_menu()
      choice = input('Which conversion would you like to do?: ')
      if choice == '1':
          km_miles()
      if choice == '2':
          miles_km()
      if choice == '3':
          kgtolb()
      if choice == '4':
          lbtokg()
      if choice == '5':
          CtoF()
      if choice == '6':
          FtoC()
      choice=input("Another conversion? (y/n)")
        