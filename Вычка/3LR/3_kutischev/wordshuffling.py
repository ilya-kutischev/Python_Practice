import sys
import random


def shuffle_words(st):
    result = []
    symbols = [' ', ',', '!', '?', '.']
    temp = []
    for i in range(len(st)):
        if st[i] in symbols:
            temp = []
            result.append(st[i])
        else:
            temp.append(st[i])
        if (i == len(st)-1 or st[i+1] in symbols) and len(temp) > 0:
            result.append(temp[0])
            end = temp[len(temp) - 1]
            del temp[len(temp) - 1]
            if len(temp) == 0:
                continue
            del temp[0]
            random.shuffle(temp)

            for j in temp:
                result.append(j)
            result.append(end)
    print(''.join(result))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        shuffle_words(sys.argv[1])
    else:
        string = input('st: ')
        shuffle_words(string)
