import sys
num = float(sys.argv[1])
x = 0
n = 1

while x<num:
    x = x + 1/n
    if x > num:
        break
    else:
        n +=1
        
print(n)