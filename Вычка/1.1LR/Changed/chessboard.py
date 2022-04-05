import sys
n = int(sys.argv[1])+1
for i in range(1, n):
    s = ''
    for j in range(1, n):
        s += str((i+j)%2) + ' '
    print(s)