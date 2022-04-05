import sys
# calc binary digits for any number
n = int(sys.argv[1])
base = int(sys.argv[2])

s = ''
while (n > 0):
    s = s + str(n % base)
    n = n // base
num = s[::-1] #реверсирует строку
print(num) 