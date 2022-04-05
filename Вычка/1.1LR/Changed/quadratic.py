import math
import sys

b = int(sys.argv[1])
c = int(sys.argv[2])
d = (b*b-4*c)

print('x^2+'+sys.argv[1]+'x+'+sys.argv[2])

if (d >= 0):

    print('x1='+str((-b+d**(0.5))/2))

    print('x2='+str((-b-d**(0.5))/2))
else:
    print('error: d < 0')