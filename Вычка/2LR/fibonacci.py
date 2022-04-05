import sys
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input('n: '))
fib = [1]
fib1 = 0
fib2 = 1
fibsum = 1
gold = []
for x in range(n-1):
    fibsum = fib1 + fib2
    fib.append(fibsum)
    fib1 = fib2
    fib2 = fibsum
    gold.append(round(fib2 / fib1, 8))  # нужно прибавить 1 к отношению, чтобы получить ЗС

print(fib)
print(gold)  # эта строка выводит отношения соседних чисел, чем больше итераций, тем ближе число к золотому сечению - 1

