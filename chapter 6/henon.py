#P165: Draw Henon Curve
'''
Draw Barnsley Fern
'''
#import random
import matplotlib.pyplot as plt



def Henon(a,b):
    x = a
    y = b
    x1 = y+1-1.4*x*x
    y1 = 0.3*x
    return x1, y1


def draw_curve(n):
    x = []
    y = []
    temp1=0.1
    temp2=0.1
    i=0
    for i in range(n):
       x1, y1 = Henon(temp1, temp2)
       temp1=x1
       temp2=y1
       x.append(x1)
       y.append(y1)
          
    return x, y

if __name__ == '__main__':
    n = int(input('Enter the number of points in the curve: '))
    x, y = draw_curve(n)
    # Plot the points
    plt.plot(x, y, 'x')
    plt.title('Henon curve with {0} points'.format(n))
    plt.show()