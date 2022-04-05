import sys
import time
name= sys.argv[1]
find = sys.argv[2]
file1 = open(name, "r")

lines = file1.readlines()
t0 = time.time()
print('linear search:')
found = []
for i in lines:
    if find == i[:len(find)]:
        found.append(i[:-1])
print(found, len(found))
print(time.time()-t0)

t0 = time.time()
print('binary search:')
found = []
mid = len(lines) // 2
low = 0
high = len(lines) - 1
while lines[mid][:len(find)] != find and low <= high:
    if find > lines[mid][:len(find)]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2


if low > high:
    print(found)
else:
    while lines[mid][:len(find)] == find:
        found.append(lines[mid][:-1])
        lines.pop(mid)
        if lines[mid+1][:len(find)] == find:
            mid+=1
        if lines[mid-1][:len(find)] == find:
            mid-=1
    print(found, len(found))
print(time.time()-t0)