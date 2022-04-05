import sys


def fibonacci(n):
    fib = [1]
    fib1 = 0
    fib2 = 1
    fibsum = 1

    for x in range(n-1):
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
            n = int(input('Input integer: '))
        print(fibonacci(n))
    except ValueError:
        print('not correct')
