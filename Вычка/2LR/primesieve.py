import sys
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input('n: '))
arr = []
arr += [x for x in range(2, n)]

for i in range(len(arr)):
    for x in arr:
        if x > arr[i] and x % arr[i] == 0:
            arr.remove(x)
    if i + 1 == len(arr):
        break

print(arr)