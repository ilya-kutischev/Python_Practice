import sys
import math
# окей, всё будем делать по формуле Кардано из гугла
a = 1
b = int(sys.argv[1])
c = int(sys.argv[2])
d = int(sys.argv[3])

print('x^3 + ' + str(b) + 'x^2 + ' + str(c) + 'x + ' + str(d) + ' == 0')
p = (3*a*c - b**2)/(3*a**2)
q = (2*b**3-9*a*b*c+27*(a**2)*d)/(27*a**3)
Q = ((p/3)**3)+(q/2)**2

al = ((-q/2)+Q**(1/2))**(1/3)
print('alpha = '+ str(al))
bt = ((-q/2)-Q**(1/2))**(1/3)
print('beta = '+ str(bt))


y1 = al + bt
y2 = -((al + bt)/2) + ((al-bt)*3**(1/2))/2
y3 = -((al + bt)/2) - ((al-bt)*3**(1/2))/2


print('y1 = ' + str(y1))
print('y2 = ' + str(y2))
print('y3 = ' + str(y3)) 

x1 = y1 - b/(3*a)
x2 = y2 - b/(3*a)
x3 = y3 - b/(3*a)

print('\n\nx1 = ' + str(x1))
print('x2 = ' + str(x2))
print('x3 = ' + str(x3)) 
#изза степеней и комплексных дробных иногда появляются расхождения с ответом