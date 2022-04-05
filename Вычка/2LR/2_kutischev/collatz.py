import sys
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input('n: '))
arr = [n]
while n > 1:
    if n % 2 == 0:
        n /= 2
    elif n % 2 == 1:
        n = 3*n + 1
    arr.append(int(n))

print(arr)
print(str(len(arr))+' # длина последовательности')
print(str(max(arr))+' # наибольший элемент последовательности')

