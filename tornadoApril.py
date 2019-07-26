#Tornado Plotter and Averages
#Giancarlo Fruzzetti

#Plots and gives stats on monthly tornados 
#for NC in April from 1952-2014
#using Numpy arrays

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

global filename1
filename1="tornadosapril1952to2014nc.txt"

global filename2
filename2="flhurricanes1900-2018.txt"

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

def NCtornados(file):
      data=file.readlines() #read lines in block
      file.close()
      data, n =readxy(data) #process data into a list
      #print(n)
      del(data[n]) #removes the EOF from the file
      #print(data)
      tornados=np.asarray(data,int)
      np.set_printoptions(threshold=np.inf)
      #print(tornados)
      mean=np.mean(tornados)
      median=np.median(tornados)
      mode=stats.mode(tornados)
      variance=np.var(tornados)
      standard=np.std(tornados)
      print(f"Mean tornados: {mean}")
      print(f"Median tornados: {median}")
      print(f"Mode tornados: {mode[0]}")
      print(f"Variance of tornados: {variance}")
      print(f"Standard Deviation: {standard}")
      T=[]
      for i in range(1952, n+1952):
         T.append(i)
      #print(T)
      flatlist = [item for sublist in data for item in sublist] #makes data into a single list for plotting
      #print(flatlist)
      plt.title("Plot of April tornados for NC since 1952")
      plt.xlabel("Year since 1952")
      plt.ylabel("Total tornados")
      plt.bar(T, flatlist)
      plt.xticks(rotation="90")
      plt.grid(True)
      return(plt)
    
def FLhurricanes(file):
      year=[]
      strikes=[]
      for line in file.readlines():
          fields = line.split()
          year.append(fields[0])
          strikes.append(fields[1])
      file.close()
      year=year[3:]  #these slice off text at top of datafile
      strikes=strikes[3:]
      strikes=[int(i) for i in strikes]
      print(year)
     # print(type(strikes[0]))
      #print(strikes)
      hurrs=np.array(strikes) #convert to numpy array for statistical calculations
      #np.set_printoptions(threshold=np.inf)
      #print(tornados)
      mean=np.mean(hurrs)
      median=np.median(hurrs)
      mode=stats.mode(hurrs)
      variance=np.var(hurrs)
      standard=np.std(hurrs)
      print(f"Mean Florida Hurricanes since 1900: {mean}")
      print(f"Median Florida Hurricanes since 1900: {median}")
      print(f"Mode Florida Hurricane strikes since 1900: {mode[0]}")
      print(f"Variance of hurricanes since 1900: {variance}")
      print(f"Standard Deviation: {standard}")
      T=[]
      for i in range(1900, len(year)+1900):
         T.append(i)
      print(T)
      #flatlist = [item for sublist in data for item in sublist] #makes data into a single list for plotting
      #print(flatlist)
      plt.title("Plot of Florida Hurricane Landfalls since 1900")
      plt.xlabel("Year")
      plt.ylabel("Total Florida Landfalls")
      plt.bar(T, strikes, width=0.5, color="red")
      plt.xticks(np.arange(1900, len(year) + 1900,5), rotation="90")
      plt.grid(True)
      return(plt)

try:
    select=int(input("Enter the file of choice, 1: NC April Tornados 2: Florida Hurricanes since 1900 by year ? "))
    if select==1:
        fl=open(filename1, "r")
    elif select==2:
        fl=open(filename2, "r")
except:
    print("File opening error, datafile does not exist!!")
else:
   if select == 1:     
       P=NCtornados(fl)
       P.show()
   if select == 2:
       p=FLhurricanes(fl)
       p.show()
       
       
      




            
            
    
    