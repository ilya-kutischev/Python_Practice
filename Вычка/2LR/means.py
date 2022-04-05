import sys
if len(sys.argv) > 1:
    arr = sys.argv[1]
else:
    arr = input('Enter array: ')

arr = arr.split(',')

averageArithmetic = 0
averageGeometric = 1
averageCuadratic = 0
for elem in arr:
    averageArithmetic += int(elem)
    averageGeometric *= int(elem)
    averageCuadratic += (int(elem)) ** 2
averageArithmetic /= len(arr)
averageGeometric = averageGeometric ** (1/len(arr))
averageCuadratic = (averageCuadratic / len(arr)) ** (1/2)

arr1 = [int(x) for x in arr]
arr1.sort()

if len(arr1) % 2 == 0:
    median = (arr1[int(len(arr) / 2)] + arr1[int(len(arr) / 2 - 1)]) / 2
else:
    median = arr1[int((len(arr) - 1) / 2)]

result = [round(averageGeometric, 2), round(averageArithmetic, 2),round(median, 2), round(averageCuadratic, 2)]
print(result)