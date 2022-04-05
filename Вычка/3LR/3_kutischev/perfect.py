import sys


def sum_divisors(n):
    sum_div = 0
    if n == 1:
        return 1
    for div in range(1, n // 2 + 1):
        if n % div == 0:
            sum_div += div
    return sum_div


def find_perfect_nums(n):
    perfect = []
    for i in range(1, n):
        if i == sum_divisors(i):
            perfect.append(i)
    print(perfect)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        find_perfect_nums(int(sys.argv[1]))
    else:
        n = int(input('n: '))
        find_perfect_nums(n)