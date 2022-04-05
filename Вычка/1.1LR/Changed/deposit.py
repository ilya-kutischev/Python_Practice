import sys
n = int(sys.argv[1])
y = int(sys.argv[2])
p = int(sys.argv[3])/100#тут указываем в обычных процентах, например 30, а не 1.3
per = 12
al = 0
if len(sys.argv)>4:
    per = int(sys.argv[4])#тут указываем на каких периодах будет зачисляться процент, если каждый месяц, то 12 и тд.
    al = int(sys.argv[5])
for x in range(y*per):
    n = n * (1+p/100*per)
    if al:
        print('The sum after '+str(x)+' periods = '+str(n))

print('The sum after all periods = '+str(n))
#можно заметить, что при пересчёте сложного процента
#чем больше периодов начисления- тем больше сумма