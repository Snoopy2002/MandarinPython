# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 18:41:10 2019

@author: Snoopy
"""

import pyfiglet as F
import termcolor as T
import sys

try:
    file=open("fontdata.txt", 'r')
except:
    print("Error, text data file fontdata.txt not found.")
    sys.exit(0)
    
document=file.readlines()
print("Available Fonts Are")
for line in document:
    line.rstrip('\n')

for line in document: #format list of fonts
    print(line, end='', flush=True)
   
    
fnt=input("Choose a font from the above list: ")
text=input("Enter a string to print out: ")
customfigure=F.figlet_format(text, font=fnt)
c=input("Choose a color: (grey/red/green/yellow/blue/magenta/cyan) ")
wordonpage=T.colored(customfigure, color=c)
print(wordonpage)
file.close()

