# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:44:43 2018
Problem 6.4.3 Scientific Programming with Python
"""

import sympy
import pylab
import numpy as np

global R
R=.08205

def VDWp(a,b,V,T):
    P=(R*T)/(V-b) - a/(V*V)
    return(P)
    
def VDWvolume(a,b,P,T):
   V=sympy.Symbol('V')
   S=P*V*V*V-(P*b+R*T)*V*V+a*V-a*b
   X=sympy.solveset(S,V)
   return(X)
    
   
def Tc(a,b):
    tc=(8*a)/(27*R*b)
    return(tc)
    
def Pc(a,b):
    pc=a/(27*b*b)
    return(pc)

def VDWinfo():
    print("\nA modification of the ideal gas law was proposed by Johannes D. van der Waals in 1873 to take into account molecular size and molecular interaction forces.")
    print("It is usually referred to as the van der Waals equation of state. ")
    print("The constants a and b have positive values and are characteristic of the individual gas. The van der Waals equation of state approaches the ideal gas law PV=nRT as the values of these constants approach zero.")
    print("The constant a provides a correction for the intermolecular forces. Constant b is a correction for finite molecular size,")
    print("and its value is the volume of one mole of the atoms or molecules.")
    print("For temperatures below Tc and Pc, all solutions are real and the smallest value is molar volume of the liquid phase.")
    print("With the largest value as the molar volume of the gas phase.")
    print("For temperatures or pressures above Tc, Pc, only 1 root is real and gives molar volume of the the gas.")
    return()
    
def VDWplot(a,b):
    
    n=2000
    compound=input("Enter the compound name: ")
    temp=int(input("Enter the Temperature in K for the isotherm: "))
    vmin=float(input("Enter the minimum volume for the plot:" ))
    vmax=float(input("Enter the maximum volume for the plot: "))
    x=pylab.linspace(vmin, vmax, n)
    y1=(R*temp)/(x-b) - a/(x*x) #Van der Waals isotherm
    y2=(R*temp)/x #Ideal Gas equation isotherm
    pylab.xlabel("Volumes in L for " + compound)
    pylab.ylabel("Pressures in atm")
    pylab.title("Isotherms at Kelvin " + str(temp))
    pylab.plot(x,y1,label='Van der Waals', color='g', linewidth=3)
    pylab.plot(x,y2, label='Ideal Gas', color='r', linewidth=3)
    pylab.legend(loc='upper left')
    pylab.show()
    return()
    
def fillarray(vdwdata):
    fname="vdwconstants.txt" 
    molecules=np.loadtxt(fname, dtype=vdwdata)
    return(molecules)
    
def printchoices(moldata):
    print("Your molecule choices are: ")
    i=0
    print("Formula\t\tName\t\t\ta\t\tb")
    for i in range(0, len(moldata)):
         print("{:10s} {:30s} {:.4f} \t {:.4f}".format(moldata[i][0], moldata[i][1], moldata[i][2], moldata[i][3]))
    return()
    
if __name__ == "__main__":  
    X=[]
    VDWdata=[('Formula', '|U8'), ('Compound', '|U40'), ('a', 'f8'),('b', 'f8')]
    moldata=fillarray(VDWdata)
    printchoices(moldata)
    a=float(input("Enter the value for a in L^2*bar/mol^2 for the molecule: "))
    a=a*0.986
    b=float(input("Enter the value for b in L/mol for the molecule: ")) 
    print("The temperature critical point of the compound in Kelvin is: ", Tc(a,b))
    print("The pressure critical point of the compound in atm is: ", Pc(a,b))
    print("Now will determine two different molar volumes at two different temperatures and pressures")
    for i in range(0,2):
      T=float(input("Enter the T in Kelvin: "))
      p=float(input("Enter the pressure in atm: "))
      X.append(VDWvolume(a,b,p,T))
    VDWinfo()
    print("The molar volumes at P1, T1, and P2, T2 are: ", X )
    ch=input("Do you want to plot isotherms? (y/n)")
    if ch == 'y':
      try:
         VDWplot(a,b)
      except:
         print("Error in plotting.")
    
    

    

    

