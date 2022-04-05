def decorator(filename, parser):
    def get_ints(func):
        list = []
        with open('func.txt', 'r', encoding='utf-8') as g:
            nums = g.readline()
            while nums:
                if nums[len(nums)-1] == '\n':
                    nums = nums[:len(nums)-1]
                else:
                    nums = nums[:]
                nums = parse_st(nums)
                list += [func(*nums)]
                nums = g.readline()
                if nums =='\n' or nums == '':
                    break
        return list
    return get_ints


def parse_st(curr):
    ls = []
    nums = curr.split(' ')
    for i in nums:
        ls +=[(int(i))]
    return ls


@decorator("func.txt", parse_st)
def summa(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(summa)

