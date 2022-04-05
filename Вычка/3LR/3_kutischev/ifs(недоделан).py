import sys
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
data =[]
with open("D:\\python\\Вычка\\3LR\\fern.txt") as f:
    data = f.readlines()
print(data)

probabilities = [float(x) for x in data[0][:-1].split(' ')]
print(probabilities)

cx = [[float(x) for x in data[2][:-1].split(' ')],[float(x) for x in data[3][:-1].split(' ')],[float(x) for x in data[4][:-1].split(' ')],[float(x) for x in data[5][:-1].split(' ')]]
print(cx)
cy = [[float(x) for x in data[7][:-1].split(' ')],[float(x) for x in data[8][:-1].split(' ')],[float(x) for x in data[9][:-1].split(' ')],[float(x) for x in data[10][:-1].split(' ')]]
print(cy)
fig, ax = plt.subplots()
fig.suptitle('Animation of fractal')
x, y = [0], [0]
ln, = plt.plot(x, y, 'bo', markersize=1)


def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ln,


def animate(i):
    num = random.randint(1,100)
    if num <= probabilities[0]*100:
        r = 0
    elif num <= probabilities[1]*100 + probabilities[0]*100:
        r = 1
    elif num <= probabilities[0]*100 + probabilities[2]*100 + probabilities[1] * 100:
        r = 2
    else:
        r = 3
    x.append(cy[r][0]*x[-1] + cx[r][1]*y[-1] + cx[r][2])
    y.append(cy[r][0] * x[-1] + cx[r][1] * y[-1] + cx[r][2])
    ln.set_data(x, y)
    print(x[-1],y[-1])
    return ln,


ani = FuncAnimation(fig, animate, init_func=init, interval=1)

plt.show()