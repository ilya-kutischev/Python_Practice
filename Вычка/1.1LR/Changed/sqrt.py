#f(x) = x^2 - c
#f'(x) = 2x
#пусть начальное приближение x_n = 1
import sys
import math
c = float(sys.argv[1])
#c = float(sys.argv[1])
t = c
eps = 1e-15
while abs(t - c/t) > eps:

    t = (t + c/t) / 2.0

print(t)

xn = 1
fx = 1    #объявим переменные, для того чтобы начать цикл.
dfx = 1
while abs(fx/dfx) > eps:
    fx = xn*xn - c  #подстановка в функуию
    dfx = 2 * xn    #подстановка в производную
    h = fx/dfx      
    xn = xn - h
    
    
print(xn)