import sys
import random
secret = []
secret.append(random.randint(0, 9))
while True:
    b = random.randint(0, 9)
    if b not in secret:
        secret.append(b)
    if len(secret) == 4:
        break
print('я загадал число!')
tries = 0
while True:
    num = int(input('введи число: '))
    num_list = []
    cows = 0
    bulls = 0
    while num:
        num_list.append(num % 10)
        num = num // 10
    num_list.reverse()
    temp = 0
    for i in num_list:
        if i == secret[temp]:
            bulls += 1
        elif i in secret:
            cows += 1
        temp += 1
    tries += 1
    if num_list == secret:
        print(f'вы угадали число за {tries} опыток')
        break
    else:
        print(f'у вас {bulls} быков и {cows} коров')