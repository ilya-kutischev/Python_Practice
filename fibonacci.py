import sys


def fibonacci(n: int):
    if n == 0:
        return [0]
    if n < 0:
        return 'not correct'
    fib = [0]
    fib1 = 0
    fib2 = 1
    for x in range(n):
        if x == 1:
            fib.append(fibsum)
            continue
        fibsum = fib1 + fib2
        fib.append(fibsum)
        fib1 = fib2
        fib2 = fibsum
    return fib


if __name__ == '__main__':

    try:
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = int(input('Input positive integer: '))
        print(fibonacci(n))
    except ValueError:
        print('not correct')
