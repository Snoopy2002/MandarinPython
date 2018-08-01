# Henon's function

import random
import math
import matplotlib.pyplot as plt

def transformation_1(p):
    x = p[0]
    y = p[1]
    x1 = .5+x 
    y1 = y
    return x1, y1

def transformation_2(p):
    x = p[0]
    y = p[1]
    x1 = math.sqrt(2)+x
    y1 = y+1
    return x1, y1

def transformation_3(p):
    x = p[0]
    y = p[1]
    x1 = .5+x
    y1 = 0.5+y
    return x1, y1


def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

def transform(p):
    # list of transformation functions
    transformations = [transformation_1, transformation_2,
                           transformation_3]
    probability = [0.33,.33,.33]
    # pick a random transformation function and call it
    tindex = get_index(probability)
    t = transformations[tindex]
    x, y = t(p)
    return x, y

def draw_triangle(n):
    # We start with (0, 0)
    x = [0]
    y = [0]
    x1, y1 = 0,0
    for i in range(n):
       x1, y1 = transform((x1, y1))
       x.append(x1)
       y.append(y1)
    return x, y

if __name__ == '__main__':
    n = int(input('Enter the number of points in the Triangle: '))
    x, y = draw_triangle(n)
    # Plot the points
    plt.plot(x, y, 'x')
    plt.title('Triangle with {0} points'.format(n))
    plt.show()