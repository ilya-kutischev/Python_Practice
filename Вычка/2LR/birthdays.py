import sys, random
if len(sys.argv) > 2:
    n = int(sys.argv[1])
    trials = int(sys.argv[2])
else:
    n = int(input('n: '))
    trials = int(input('trials: '))
peoplesCount = []
probability = 1
count = 1
while True:
    probability *= (n-count) / n
    count += 1
    if probability < 0.5:
        break
print(str(count)+' # это корректное значение для 365 дней')
for x in range(trials):
    fl = 1
    birthdays = []
    while fl:
        birthdays.append(random.randint(1, n))
        for i in birthdays:
            if birthdays.count(i) > 1:
                fl = 0
                break
    peoplesCount.append(len(birthdays))
print(str(peoplesCount) + ' # ' + str(trials) + ' попыток')
middle = 0
for x in peoplesCount:
    middle += x
middle /= len(peoplesCount)
print(str(middle) + ' # среднее значение массива')