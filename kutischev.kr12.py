class Iterator:

    def __init__(self, fill = 0, *args):
        self.max_len = len(args[0])
        for i in range(0, len(args)):
            if len(args[i]) > self.max_len:
                self.max_len = len(args[i])
            if hasattr(args[i], '__iter__') and not isinstance(args[i], str):
#               print('Iterable')
                for elem in args[i]:
                    if elem == args[i]:
                        raise ValueError('Cyclic reference detected')
        self.arg = args
        self.fill = fill
        self.count = 0

    def __next__(self):
        tupls = []
        args = self.arg
        count = self.count
        while self.max_len > count:
            for i in range(len(args)):
                if len(args[i]) - 1 < count:
                    tupls.append(self.fill)
                else:
                    tupls.append(args[i][count])
            count+=1
            self.count = count
            return tuple(tupls)
        else:
#            print('StopIteration')
            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == '__main__':
    asasas = 10
    fill = 0
    itr = Iterator(fill,[1,2,3],(1,2,3,4),['5', 's', 'f', 122, asasas])
    lst = []
    for i in itr:
        lst.append(i)
    print(lst)
    asasas = [0,[6,['u']]]
    it = Iterator(fill,[1,2,3],['5', 's', 'f', 123, asasas])
    lst = []
    for i in it:
        lst.append(i)
    print(lst)