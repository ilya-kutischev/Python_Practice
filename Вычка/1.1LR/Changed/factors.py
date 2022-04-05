import sys


# factor n, e.g. 36 = 2 * 2 * 3 * 3

#n = int(input('n: '))
n = int(sys.argv[1])


factor = 2

s = ''
n1 = n

while (n**0.5+1 >= factor): #улучшенный цикл, проверяем делители до корня из числа
#прибавим 1, чтобы убрать погрешность при извлечении корня
        while (n % factor == 0):

                s += str(factor) + ' '
                n = n / factor

        factor += 1


print(s+''+str(int(n))) #последним делителем числа будет само число в остатке

#n = n1
#factor = 2   #старый цикл, для сравнения по времени
#s = ''
#while (n > 1):

#        while (n % factor == 0):

#                s += str(factor) + ' '

#                n //= factor

#        factor += 1


#print(s)