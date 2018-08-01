#P151: Drawing a Circle
'''
Example of using matplotlib's Circle patch
'''
from matplotlib import pyplot as plt
from matplotlib import animation

def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,

def animate(i):
    patch.radius=i*0.010
    return patch,

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
ax.set_aspect('equal')
patch = plt.Circle((0, 0), 0.75, fc='r', ec='b')



anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=10,
                               blit=True)

plt.show()