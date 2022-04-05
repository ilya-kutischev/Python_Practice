import sys
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input('n: '))
for a in reversed(range(2 ** n)):
    b = ''
    while a > 0:
        b = str(a % 2) +','+ b
        a = a // 2
    b = b.split(',')
    b.remove('')
    b = [int(x) for x in b]
    while len(b) < n:
        b.insert(0, 0)
    print(b)