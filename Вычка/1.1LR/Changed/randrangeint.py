import sys
import random
min = int(sys.argv[1])
max = int(sys.argv[2])
rand_num = random.randrange(min, max)
print(rand_num)
#random.randrange(<Начало>, <Конец>, <Шаг>)