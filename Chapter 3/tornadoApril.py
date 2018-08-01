#Tornado Plotter and Averages
#Giancarlo Fruzzetti

#Plots and gives stats on monthly tornados 
#for NC in April from 1952-2014
#using Numpy arrays

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

global filename
filename="tornadosapril1952to2014nc.txt"

def readxy(data): #general function to strip numbers out of a text file line by line
    results=[]
    count=0
    for line in data:
        nextline=[]
        cells=line.strip().split(" ") #split data by spaces
        for cell in cells:
            try:
                value=int(cell.strip())#convert to int
                count=count+1 #counts number of lines read in
            except: #if this fails use original
                value=cell
            nextline.append(value)
        results.append(nextline)
    return results, count

fl=open(filename, "r")
data=fl.readlines() #read lines in block
fl.close()
data, n =readxy(data) #process data into a list
#print(n)
#rint(data)
del(data[n]) #removes the EOF from the file
tornados=np.asarray(data,int)
np.set_printoptions(threshold=np.inf)
#print(tornados)
mean=np.mean(tornados)
median=np.median(tornados)
mode=stats.mode(tornados)
variance=np.var(tornados)
standard=np.std(tornados)
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Variance: ", variance)
print("Standard Deviation: ", standard)
T=range(1952,n+1952)
plt.title("Plot of April tornados for NC since 1952")
plt.xlabel("Year since 1952")
plt.ylabel("Total tornados")
plt.bar(T, tornados)
plt.show()




            
            
    
    