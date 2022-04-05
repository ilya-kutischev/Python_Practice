import sys

n = int(sys.argv[1])

matrix = [[0 for y in range(n)] for x in range(n)]
j = 0


def spiral(matr, j, n, start):
    for i in range(n):
        matr[j][i + j] = start
        start += 1

    for i in range(1, n):
        matr[i + j][n + j - 1] = start
        start += 1

    for i in range(1, n):
        matr[n - 1 + j][n - i - 1 + j] = start
        start += 1

    for i in range(1, n - 1):
        matr[n - i - 1 + j][j] = start
        start += 1

    if n == 2 or n == 1:
        return
    else:
        j += 1
        spiral(matr, j, n - 2, start)


spiral(matrix, j, n, 1)
for im in range(n):
    print(matrix[im])
