#trajectory plotter

from matplotlib import pyplot as plt
import math
#import sympy as sp
global g
g=9.8

def draw_graph(x,y): #code to draw the projgectile graphs
    plt.plot(x,y)
    plt.xlabel('x-coord in m')
    plt.ylabel('y-coord in m')
    plt.title('Projectile Motion of a ball')
    
    
def frange(start, final, intvl): #sets up the range (x axis) in increments of interval units
    numbers=[]
    while start < final:
       numbers.append(start)
       start=start+intvl
    return numbers

def draw_trajectory(v0, theta): #draws the graph by computing the time of flight, 
    theta=math.radians(theta) #and x and y values and then returns the total time of flight to calling function
    tflight=(2*v0*math.sin(theta))/g #see if students can add this line
    intervals=frange(0, tflight, 0.001)
    x=[]
    y=[]
    for t in intervals: #see if students can add these two lines
        x.append(v0*math.cos(theta)*t)
        y.append((v0*math.sin(theta)*t) - (0.5*g*t*t))

    draw_graph(x,y)
    return(tflight)
    
try: #students will consider the needed inputs and call for them
    ttraj=input("Enter the total number of trajectories at a specific angle you want to input: ")
    ttraj=int(ttraj)
    theta=input("Enter the initial angle of projection, theta: ")
    theta=float(theta)
    v0list=[]
    for i in range(ttraj):
       v0=input("Enter initial velocity v0 in m/sec: ")
       v0=float(v0)
       v0list.append(v0)
    
except:
    print("Invalid input for v0 or theta or both.")
else:
      for v0 in v0list: #students try to fill the next 4 lines
            tflight=draw_trajectory(v0, theta) #total time of flight
            R=(v0*v0)/g * (math.sin(2*math.radians(theta))) #range equation
            tmax=tflight/2 #time of maximum height
            ymax=(v0*math.sin(math.radians(theta))*tmax)-(0.5*g*tmax*tmax) #maximum height reached in meters
            print("Total time of flight in air is ", tflight, " seconds for " , v0)
            print("Total range of the projectile is ", R, " meters for ", v0)
            print("Maximum height reached during flight is: ", ymax, "meters for ", v0)
plt.show()
plt.savefig("trajectories.jpg")

    

