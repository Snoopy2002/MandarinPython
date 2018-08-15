# -*- coding: utf-8 -*-
"""
Planck Law Plotter
"""

import pylab
import scipy.constants
import numpy as np

global U
U=(scipy.constants.h*scipy.constants.c)/scipy.constants.Boltzmann

def Normalize(b):
    Bnorm=[]
    Min=min(b)
    Max=max(b)
    
    for i in range(0,len(b)):
       Bi=(b[i]-Min)/(Max-Min)
       Bnorm.append(Bi)
       
    return(Bnorm)
    
def RadianceArray(xvals, U):
    B=(2*scipy.constants.Planck*scipy.constants.c*scipy.constants.c)/(xvals*xvals*xvals*xvals*xvals)*1/(np.exp(U/xvals)-1)
    return(B)
    

T=float(input("Enter the temperature of the first blackbody in Kelvin: "))
T2=float(input("Enter the temperature of the second blackbody in Kelvin: "))
T3=float(input("Enter the temperature of the second blackbody in Kelvin: "))
V1=str(int(T))+' K' #for the plot legend text strings
V2=str(int(T2))+' K'
V3=str(int(T3))+' K' 
U2=U*1/T #compute constant part of the radiance equation 1
U3=U*1/T2 #compute constant part of the radiance equation 
U4=U*1/T3
n=100000
lmin, lmax = 0.000000001,.00001
t=pylab.linspace(lmin, lmax, n)
B=(2*scipy.constants.Planck*scipy.constants.c*scipy.constants.c)/(t*t*t*t*t)*1/(np.exp(U2/t)-1)
B2=(2*scipy.constants.Planck*scipy.constants.c*scipy.constants.c)/(t*t*t*t*t)*1/(np.exp(U3/t)-1)
B3=(2*scipy.constants.Planck*scipy.constants.c*scipy.constants.c)/(t*t*t*t*t)*1/(np.exp(U4/t)-1)
B=RadianceArray(t,U2)
B2=RadianceArray(t,U3)
B3=RadianceArray(t,U4)
Bnorm=Normalize(B)
B2norm=Normalize(B2)
B3norm=Normalize(B3)
pylab.plot(t,Bnorm, label=V1, color='g', linestyle='--')
pylab.plot(t,B2norm, label=V2, color='r', linestyle='-')
pylab.plot(t,B3norm, label=V3, color='b', linestyle='-.')
pylab.title("Normalized Blackbody radiation curves")
pylab.legend()
pylab.xlabel('Wavelength in M')
pylab.ylabel('Surface Radiance in W/(sr*m^2*Hz)')
pylab.show()
 