import sys


def count_substring(st, subst):
    count = 0
    for i in range(len(st) - len(subst)+1):
        if subst == st[i : i + len(subst)]:
            count += 1
    return count


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(count_substring(str(sys.argv[1]), str(sys.argv[2])))
    else:
        st = input('st: ')
        sub_st = input('sub_st: ')
        print(count_substring(st, sub_st))
