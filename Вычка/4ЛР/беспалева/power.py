import sys


def exp(b, n):
    if n==0:
        return 1
    if n%2==0:
        return exp(b, n/2)**2
    return b*exp(b, n-1)

b = int(sys.argv[1])
n = int(sys.argv[2])

print(exp(b, n))