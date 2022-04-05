import sys
import math


def func(x):
        if x == 0:
                return 1
        else:
                return math.sin(x) / x


if len(sys.argv) > 3:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    n = int(sys.argv[3])
else:
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    n = int(input('Enter n: '))
h = (b - a) / n
x = a
s_trap = 0
while (x < b):
        s_trap += (func(x) + func(x + h)) * h / 2
        x += h
print(s_trap)
