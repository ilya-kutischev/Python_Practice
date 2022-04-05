import random
import sys
stake = int(sys.argv[1])
goal = int(sys.argv[2])
continue_play = 0
if len(sys.argv)>3:
    continue_play = int(sys.argv[3])
fl = 1
while fl:
    trails = 0
    s = stake
    maxS = stake
    while s and s < goal:
        trails += 1 #для подсчёта среднего количества итераций
        if s > maxS: #для вычисления максимальных значений
            maxS = s
        if random.randrange(2):
            s += 1
        else:
            s -= 1
        
    if s:
        print('you win!')
    else:
        print('you lose(')
    print('количество итераций: '+str(trails))
    print('максимальное значение: '+str(maxS))
    if continue_play !=0:
        fl = int(input('wanna continue? 1-y,0-n: '))
    else:
        fl = 0
#на практике получилось вероятность около 10% увелисить свой выигрыш в 10 раз
#для того чтобы игрок выиграл 10 или проиграл 10 очков в среденем надо около 100 итераций, при этом значение очень сильно колебается.
#при параметрах stack= 10 trails= 20, среднее максимальное колеблется около 18