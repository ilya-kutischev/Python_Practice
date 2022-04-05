import random
player1 = 0 #игрок не меняет решение
player2 = 0 #игрок меняющий решение
n = int(input('number of iterations: '))
for x in range(n):
    winDoor = random.randrange(1,4)
    p1Choice = random.randrange(1,4)
    p2Choice = random.randrange(1,4)
    if p2Choice == 1 and winDoor == 1:
        p2Choice = random.choice([2,3]) #если его выбор 1 и совпадает с победным, то он все равно меняет дверь
    elif p2Choice == 2 and winDoor == 2:
        p2Choice = random.choice([1,3])
    elif p2Choice == 3 and winDoor == 3: #я это прописал, хоть это не имеет смысла
        p2Choice = random.choice([1,2]) #если 2 игрок изначально угадал, то он проиграет
    # но если 2 игрок изначально выбрал неверную дверь, то после, поменяв, в любом случае выиграет
    elif p2Choice != winDoor:
        p2Choice = winDoor
    #присваиваем очки, если игроки угадали
    if p2Choice == winDoor:
        player2 += 1
    if p1Choice == winDoor:
        player1 += 1
        
print('игрок 1 выиграл в '+str(player1*100/n)+'%')#подсчет очков и вывод
print('игрок 2 выиграл в '+str(player2*100/n)+'%')
#что интересно, вероятность выигрыша 2 игрока в данной программе в среднем 72%, хотя по теории вероятности должно быть 66.6%
#возможно это связано с предпочтениями функции ramdom