import sys  # Пример ввода 0 1,2,3
if len(sys.argv) > 1:
    player = int(sys.argv[1])
    first_stack = int(str(sys.argv[2]).split(',')[0])
    second_stack = int(str(sys.argv[2]).split(',')[1])
    third_stack = int(str(sys.argv[2]).split(',')[2])

binary_dif= first_stack ^ second_stack ^ third_stack
if player == 0:
    if binary_dif > 0:
        if first_stack ^ binary_dif < first_stack:
            difference = first_stack - (first_stack ^ binary_dif)
            first_stack -= difference
            took = first_stack
            number = 1
        elif second_stack ^ binary_dif < second_stack:
            difference = second_stack - (second_stack ^ binary_dif)
            second_stack -= difference
            took = second_stack
            number = 2
        else:
            difference = third_stack - (third_stack ^ binary_dif)
            third_stack -= difference
            took = third_stack
            number = 3
    else:
        first_stack -= 1
        difference = 1
        number = 1
        took = first_stack
    print("Me-" + str(difference) + " stones from " + str(number) + " stack, now situation: " + str(first_stack) + ', '+str(second_stack)+', '+str(third_stack))
    player = 1
if player == 1:
    while first_stack + second_stack + third_stack > 0:
        step = 2
        number = 0
        while number < 1 or number > 3:
            number = int(input("Choose stack: "))
            if number == 1 and not first_stack or number == 2 and not second_stack or number == 3 and not third_stack:
                print("Choose another")
                number = 0
        contin = True
        while contin:
            if number == 1:
                took = first_stack
            elif number == 2:
                took = second_stack
            else:
                took = third_stack
            difference = int(input("Choose Amount less then " + str(took)+": "))
            if difference > 0 and difference <= took:
                if number == 1:
                    first_stack -= difference
                    took = first_stack
                elif number == 2:
                    second_stack -= difference
                    took = second_stack
                else:
                    third_stack -= difference
                    took = third_stack
                print("-" + str(difference) + " stones from " + str(number) + " stack, now situation: " + str(first_stack) + ', ' + str(second_stack) + ', ' + str(third_stack))
                contin = False
        if first_stack + second_stack + third_stack > 0:
            step = 1
            binary_dif = first_stack ^ second_stack ^ third_stack
            if binary_dif > 0:
                if first_stack ^ binary_dif < first_stack:
                    difference = first_stack - (first_stack ^ binary_dif)
                    first_stack -= difference
                    took = first_stack
                    number = 1
                elif second_stack ^ binary_dif < second_stack:
                    difference = second_stack - (second_stack ^ binary_dif)
                    second_stack -= difference
                    took = second_stack
                    number = 2
                else:
                    difference = third_stack - (third_stack ^ binary_dif)
                    third_stack -= difference
                    took = third_stack
                    number = 3
            else:
                if first_stack > 0:
                    first_stack -= 1
                    number = 1
                    took = first_stack
                elif second_stack > 0:
                    second_stack -= 1
                    number = 2
                    took = second_stack
                else:
                    third_stack -= 1
                    number = 3
                    took = third_stack
                difference = 1
            print("-" + str(difference) + " stones from " + str(number) + " stack, now situation: " + str(first_stack) + ', ' + str(second_stack) + ', ' + str(third_stack))
if step == 1:
    print("You lose")
else:
    print("you win!")
