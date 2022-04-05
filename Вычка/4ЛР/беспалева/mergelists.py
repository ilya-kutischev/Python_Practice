import sys
import random
n = int(sys.argv[1])
arr1 = [random.randint(0,n+1) for i in range(random.randint(1,n+1))]
arr2 = [random.randint(0,n+1) for i in range(random.randint(1,n+1))]
arr1.sort()
arr2.sort()
print(arr1)
print(arr2)
lst = [0]*(len(arr1)+len(arr2))
i = 0
j = 0
k = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        lst[k] = arr1[i]
        i += 1
    else:
        lst[k] = arr2[j]
        j = j + 1
    k = k + 1
while i < len(arr1):
    lst[k] = arr1[i]
    i = i + 1
    k += 1
while j < len(arr2):
    lst[k] = arr2[j]
    j += 1
    k += 1

print(lst)