#Earth Similarity Index
global rwt 
rwt=0.57
global dwt 
dwt=1.07
global vesc
vesc= 0.7
global ST
ST= 5.58
global n 
n=4.0

import numpy as np
import math

def CompESI(parray):
    ESI=np.empty(12)
    similarities=[]
    i=1
    print("Earth Similarity Index Values")
    print("=============================")
    outfile=open("similarities.txt",'w')
    for i in range(12):
        #print(parray[i][2], parray[i][3], parray[i][5],parray[i][7])
        ESI[i]=math.pow((1-math.fabs((parray[i][2]-parray[0][2])/(parray[i][2]+parray[0][2]))),float(rwt/n))+math.pow(1-math.fabs((parray[i][3]-parray[0][3])/(parray[i][3]+parray[0][3])),float(dwt/n))+math.pow(1-math.fabs((parray[i][5]-parray[0][5])/(parray[i][5]+parray[0][5])),float(vesc/n))
        math.pow((1-math.fabs((parray[i][7]-parray[0][7])/(parray[i][7]+parray[0][7]))),float(ST/n))
        ESI[i]=ESI[i]-2
        similarities.append(parray[i][0]) #copy to list and write out to text file
        similarities.append(ESI[i])
    for item in similarities:
        outfile.write("%s\n" %item)
        
        
        

try:
    planetdata=np.dtype([('PlanetName', '|S14'),('mass', 'float'), ('radius', 'float'), ('density', 'float'), ('g', 'float'), ('vesc','float'),('sun distance', 'float'),('Tsurf', 'float'), ('Teq', 'float')])
except:
    print("Invalid input\n")
else:
    fname="planetsdata.txt"
    planetarray=np.loadtxt(fname,dtype=planetdata, skiprows=3)#start loading at 3d row of datafile
   # print(planetarray)
    CompESI(planetarray)
    print("Results written to similarities.txt, program complete.")
