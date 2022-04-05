import sys


def check_result(array, member):
    for i in range(len(array)):
        if member<= array[i+1] and member>= array[i]:
            array.insert(i+1, member)
        if not i:
            difference1 = array[i+1]-array[i]
        difference = array[i + 1] - array[i]
        if difference != difference1:
            return False
        else:
            difference1 = difference
    return True


def find_missing_el(array, n):
    neibhor = array[n -1] - array[0]
    difference = int((neibhor) / n)
    return find_missing_member(array, 0, n- 1, difference)


def find_missing_member(array, left, rigth, difference):
    if left >= rigth:
        return sys.maxsize
    mddl = (rigth - left)/2
    middle = int((mddl)+left)
    dif = array[middle +1] - array[middle]
    if dif != difference:
        return  difference+array[middle]
    dif = array[middle]- array[middle - 1]
    if dif != difference and middle > 0:
        return array[middle- 1] + difference
    dif = array[0]+ middle * difference
    if array[middle] == dif:
        return find_missing_member(array, middle+ 1, rigth, difference)
    return find_missing_member(array, left, middle- 1, difference)


a = sys.argv[1]
array = [int(x) for x in a.split()]
# array = [1, 2, 3, 5, 6]
miss = find_missing_el(array, len(array))
if check_result(array, miss):
    print(miss)
else:
    print('Nothing missed')
