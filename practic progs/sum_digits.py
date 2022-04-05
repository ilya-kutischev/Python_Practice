def sum_digits(num: int)->int:    //tipe hint
    '''docstring comments'''
    digits = [int(d) for d in str(num)]  //massiv cifr
    return sum(digits)

if __name__ == '__main__':
    print(sum_digits(111))
    assert sum_digits(23) == 5
    assert sum_digits(56) == 10 //proverka