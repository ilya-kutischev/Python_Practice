import sys
def get_gcd(a:int, b:int): #int
    while(min(a, b)): #реализуем алгоритм Евелида
        if a > b:
            a %= b
        else:
            b %= a
    if a:
        return a
    else:
        return b
    
#def get_lcm(a:int, b:int): #int
#    return a * b / get_gcd(a, b)

if __name__ == '__main__':
    first_number, second_number = sys.argv[1], sys.argv[2]
    if first_number.isdigit() and second_number.isdigit():
        print('gcd = ' + str(get_gcd(int(first_number), int(second_number))))
#        print('lcm = ' + str(get_lcm(int(first_number), int(second_number))))
    else:
        print("Input Error")  #если введены не целые числа, то выведет ошибку
    

    