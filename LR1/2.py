#ближайшее простое к данному
import sys
#import argparse можно посмотреть

def is_prime(num: int) -> bool:
    """brute force test for primarity"""
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        else:
            pass
    return True

def find_closest_prime(num: int) -> int:
    
    if num <= 1:
        return 2
    step = 0
    while True:
        if is_prime(num + step):
            return num + step
        elif is_prime(num - step):
            return num - step
        else:
            step += 1


if __name__ == '__main__':

    try:
        if len(sys.argv) == 2:
            test_number = int(sys.argv[1])
        else:
            test_number = int(input('Input integer'))
        print(f'Clothest prime to {test_number} is {find_closest_prime(test_number)}')
    except ValueError:
        print('not correct')