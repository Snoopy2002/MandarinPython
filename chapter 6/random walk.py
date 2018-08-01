#P160: Random walk of a point in a plane
#and stock price approximator
'''
Example of selecting a transformation from two equally probable
transformations
'''

import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    return x + 1, y - random.random()

def transformation_2(p):
    x = p[0]
    y = p[1]
    return x + 1, y + random.random()
    
def transformation_3(p):
    x=p[0]
    y=p[1]
    return x + 1, y - random.random()
    
def transformation_4(p):
    x=p[0]
    y=p[1]
    return x + 1, y + random.random()

def transform(p):
    # list of transformation functions
    transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    # pick a random transformation function and call it
    t = random.choice(transformations)
    x, y = t(p)
    while y < 0.01:
        t = random.choice(transformations)
        x, y = t(p)
    return x, y

def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

if __name__ == '__main__':
    # initial point
    random.seed()
    p = (0, 40)
    n = int(input('Enter the number of iterations: '))
    x, y = build_trajectory(p, n)
    # plot
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()