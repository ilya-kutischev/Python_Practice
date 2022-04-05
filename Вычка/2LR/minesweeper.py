import sys, random
if len(sys.argv) > 2:
    n = int(sys.argv[1])
    p = float(sys.argv[2])
else:
    n = int(input('n: '))
    p = float(input('p: '))
matr = []
for i in range(n + 2):
    matr.append([])
    for j in range(n + 2):
        matr[i].append(0)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if random.randint(1,100) <= p * 100:
            matr[i][j] = '*'
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if matr[i][j] == 0:
            if matr[i-1][j-1] == '*':
                matr[i][j] += 1
            if matr[i-1][j] == '*':
                matr[i][j] += 1
            if matr[i][j-1] == '*':
                matr[i][j] += 1
            if matr[i+1][j-1] == '*':
                matr[i][j] += 1
            if matr[i-1][j+1] == '*':
                matr[i][j] += 1
            if matr[i+1][j] == '*':
                matr[i][j] += 1
            if matr[i][j+1] == '*':
                matr[i][j] += 1
            if matr[i+1][j+1] == '*':
                matr[i][j] += 1
for i in range(1, n + 1):
    print(matr[i][1:-1])
