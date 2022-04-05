#{1,1,3,4} - type set, different values
def find_closest(values: set, num: int)->int:
    el_list = sorted(values)
    d_list = [abs(num - x) for x in el_list]
    return el_list[d_list.index(min(d_list))] #position of min

def find_closest1(values: set, num: int)->int:
    return min(values, key = lambda x: (abs(x - num), x)) 


if __name__ == '__main__':
    print(find_closest({-1, 0, 3, 7 ,3 ,4, 6 ,10}, -2))
    print(find_closest1({-1, 0, 3, 7 ,3 ,4, 6 ,10}, -2))