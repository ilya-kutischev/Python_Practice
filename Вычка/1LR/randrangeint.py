import sys
import random
min = int(input('min: '))
max = int(input('max: '))
rand_num = random.randrange(min, max)
print(rand_num)
#random.randrange(<Начало>, <Конец>, <Шаг>)