import sys
if len(sys.argv) > 1:
    arr = sys.argv[1]
else:
    arr = input('Enter array: ')

arr = arr.split(',')
arr = [int(x) for x in arr]
print(arr)
dict = {}
for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
maxCount = 0
max = []
for i in dict.keys():
    if dict[i] > maxCount:
        maxCount = dict[i]
        max = [i]
    elif dict[i] == maxCount:
        max.append(i)
print(max)