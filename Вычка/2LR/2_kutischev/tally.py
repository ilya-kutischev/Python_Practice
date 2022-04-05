import sys
if len(sys.argv) > 1:
    arr = sys.argv[1]
else:
    arr = input('Enter array: ')

arr = arr.split(',')
arr = [int(x) for x in arr]
arr.sort()
include = []
fl = 1
for x in arr:
    for i in include:
        if i[0] == x:
            i[1] += 1
            fl = 0
    if fl:
        include.append([x, 1])
    fl = 1
print(include)