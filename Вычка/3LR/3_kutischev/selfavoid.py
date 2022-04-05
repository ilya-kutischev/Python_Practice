import numpy as np
import matplotlib.pyplot as plt
import random


def is_point_in(wx, wy, px, py, n1):
    if px <= 0 or py <= 0 or px >= n1 or py >= n1:
       return 1
    for i in range(len(wx)):
        if px == wx[i] and py == wy[i]:
            return 1
    return 0


def random_walk(n):
    steps = []
    x, y = n//2, n//2
    walkx, walky = [x], [y]
    fl = 1
    while fl:
        choise = []
        if not is_point_in(walkx, walky, x+1, y, n):
            choise.append(1)
        if not is_point_in(walkx, walky, x, y+1, n):
            choise.append(2)
        if not is_point_in(walkx, walky, x-1, y, n):
            choise.append(3)
        if not is_point_in(walkx, walky, x, y-1, n):
            choise.append(4)
        if len(choise) == 0:
            fl = 0
            break
        new = random.choice(choise)
        if new == 1:
            x += 1
        if new == 2:
            y += 1
        if new == 3:
            x += -1
        if new == 4:
            y += -1
        walkx.append(x)
        walky.append(y)

    return [walkx, walky]


n = int(input('n: '))
walk = random_walk(n)
plt.plot(walk[0][0], walk[1][0], 'ro')  # первая точка красная
plt.plot(walk[0][-1], walk[1][-1], 'bo')  # последняя синяя
plt.plot(walk[0], walk[1])
plt.xlim(0, n)  # задаем видимый диапазон по x и y
plt.ylim(0, n)
ticks = [x for x in range(1, n+1)]
plt.xticks(ticks)  # применяем нужную сетку
plt.yticks(ticks)
plt.grid()
plt.show()