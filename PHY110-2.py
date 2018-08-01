#trajectory plotter

from matplotlib import pyplot as plt
import math
global g
g=9.8

def draw_graph(x,y): #code to draw the projectile position graph
    plt.figure(1) #allows multiple plots to display at once
    plt.plot(x,y)
    plt.xlabel('x-coord in m')
    plt.ylabel('y-coord in m')
    plt.title('Projectile Motion of a ball')
    
def draw_Penergy(a,b): #code to draw the projectile potential energy graph
    plt.figure(2)
    plt.plot(a,b, color='green')
    plt.xlabel('time in seconds')
    plt.ylabel('E in Joules')
    plt.title('Potential Energy of a Projectile in Motion')    
    
def draw_Kenergy(a,b): #code to draw the projectile potential energy graph
    plt.figure(3)
    plt.plot(a,b, color='red')
    plt.xlabel('time in seconds')
    plt.ylabel('E in Joules')
    plt.title('Kinetic Energy of a Projectile in Motion')  
    
def frange(start, final, intvl): #sets up the range (x axis) in increments of interval units
    numbers=[]
    while start < final:
       numbers.append(start)
       start=start+intvl
    return numbers

def draw_trajectory(v0, y0, theta, tflight): #draws the projectile position graph
  
    intervals=frange(0, tflight, 0.001)
    x=[]
    y=[]
    for t in intervals: 
        x.append(v0*math.cos(theta)*t)
        y.append(y0+(v0*math.sin(theta)*t) - (0.5*g*t*t))

    draw_graph(x,y)
    return

def draw_kinetic(massobj, tflight, y0, v0, theta): #draws the projectile kinetic energy graph

    intervals=frange(0, tflight, 0.1)
    a=[]
    b=[]
    for t in intervals:
       a.append(t)
       vx=v0*math.cos(theta) #x component of velocity
       vy=v0*math.sin(theta)-g*t #y-component of velocity
       KE=0.5*massobj*( vx*vx + vy*vy) #kinetic energy
       b.append(KE)
    draw_Kenergy(a,b)
    return
    

def draw_potential(massobj, tflight, y0, v0, theta): #draws the projectile potential energy graph
    
    intervals=frange(0, tflight, 0.1)
    a=[]
    b=[]
    for t in intervals:
        a.append(t)
        h=y0+(v0*math.sin(theta)*t) - (0.5*g*t*t)
        b.append(massobj*g*h)
    draw_Penergy(a,b)
    return
    
try: #attempt to get the input data
    massobj=input("Enter the mass of the object in kg: ")
    massobj=int(massobj)
    theta=input("Enter the initial angle of projection, theta in degrees: ")
    theta=float(theta)
    theta=math.radians(theta)
    v0=input("Enter initial velocity v0 in m/sec: ")
    v0=float(v0)  
    y0=input("Enter the initial height y0 in m: ")
    y0=float(y0)
    
except:
    print("Invalid input.")
    
else:
    tmax=v0*math.sin(theta)/g #time of maximum height
    ymax=y0+(v0*math.sin(theta)*tmax)-(0.5*g*tmax*tmax) #maximum height reached in meters
    tflight=tmax+math.sqrt((2*ymax)/g)
    R=(v0*math.cos(theta)*tflight) #range equation
    draw_trajectory(v0, y0, theta, tflight)
    draw_potential(massobj, tflight, y0, v0, theta)
    draw_kinetic(massobj, tflight, y0, v0, theta)
    theta=math.degrees(theta)    
    print("Total time of flight in air is ", tflight, " seconds for " , theta, "degrees.")
    print("Total range of the projectile is ", R, " meters for ", theta, " degrees. ")
    print("Maximum height reached during flight is: ", ymax, "meters for ", theta, " degrees. ")
plt.show()

    

