import sys
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input('n: '))
pascal = [1]
move = []
total = [pascal[:]]
for i in range(n - 1):
    move = pascal[:]
    move.append(0)
    pascal.insert(0, 0)

    for x in range(len(pascal)):
        pascal[x] = pascal[x] + move[x]
    total.append(pascal[:])
print(total)
