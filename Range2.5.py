class Range:

    def __init__(self, start, stop=None, step=1, my_filter=None):
        self.filter = my_filter
        if stop is None:
            stop = start
            start  = 0
        self.start, self.stop, self.step = (
            int(start), int(stop), int(step)
        )
        if not step:
            raise ValueError('Step must not be zero')
        if self.step > 0:
            step_sign = 1
        else:
            step_sign = -1
        self._len = max(
            1 + (self.stop - self.start - step_sign) // self.step, 0
        )

    def __iter__(self):
        num = self.start
        if self.step > 0:
            while num < self.stop:
                if (self.filter is not None) and (not self.filter(num)):
                    num += self.step
                else:
                    yield num
                    num += self.step
        else:
            while num > self.stop:
                if (self.filter is not None) and (not self.filter(num)):
                    num += self.step
                else:
                    yield num
                    num += self.step

    def index(self, value, start=0, stop=None):
        if start < 0:
            start = max(self._len + start, 0)
        if stop is None:
            stop = self._len
        if stop < 0:
            stop += self._len

        if isinstance(value, numbers.Integral):
            index = self._index(value)
            if start <= index < stop:
                return index
            raise ValueError('{} is not in Range'.format(value))

        i = start
        n = self.start + self.step * i
        while i < stop:
            if n == value:
                return i
            i += 1
            n += self.step
        raise ValueError('{} is not in Range'.format(value))


# making filter
def is_odd(a):
    if a % 2 == 0:
        return False
    else:
        return True


def my_filter(rule_fun, lst: list):
    for i in lst:
        if not rule_fun(i):
            lst.remove(i)
    return lst


if __name__ == '__main__':
#    example = my_filter(is_odd, list(Range(1,30,3)))
#    print(example)
    example = list(Range(10, -10, -1))
    print(example)
    example = list(Range(10,-10,-1,is_odd))
    print(example)