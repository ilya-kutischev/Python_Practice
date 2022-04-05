class Iterator:

    def __init__(self, fill = 0, *args):
        self.arg = args
        self.fill = fill
        self.max_len = len(args[0])
        self.count = 0
        for i in range(1, len(args)):
            if len(args[i]) > self.max_len:
                self.max_len = len(args[i])
        print(args)
        print("Fill", self.fill)
        print("max", self.max_len)

    def __next__(self):
        tupls = []
        args = self.arg
        while self.max_len > self.count :
            for i in range(len(args)):
                if len(args[i]) <= self.count:
                    tupls.append(self.fill)
                else:
                    tupls.append(args[i][self.count])
            self.count = self.count + 1
            return tuple(tupls)
        else:
            print('StopIteration')
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
    asasas = [0,0]
    asasas[0] = asasas
    it = Iterator(fill,[1,2,3],['5', 's', 'f', 123, asasas])
    lst = []
    for i in it:
        lst.append(i)
    print(lst)