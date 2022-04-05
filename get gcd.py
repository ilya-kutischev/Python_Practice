def get_gcd(a:int, b:int): #int
    """Function for gcd"""
    if a == 0 or b == 0 or a == b:
        return max(a, b)
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b %= a
    if a > 0:
        return a
    else:
        return b

if __name__ == '__main__':
    first_number, second_number = input("Enter two numbers split by space").split()
    if first_number.isdigit() and second_number.isdigit():
        print(get_gcd(int(first_number), int(second_number)))
    else:
        print("Input Error")