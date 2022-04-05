class MyDefaultdict(dict):
    @staticmethod
    def exception_fun():
        return 'object not found'

    def __init__(self, *args, **kwargs):
        if 'default' in kwargs:
            self.default = kwargs['default']
            del kwargs['default']
        else:
            self.default = None
        dict.__init__(self, *args, **kwargs)

    def __repr__(self):
        return str(self.default, dict.__repr__(self))

    def __str__(self):
        return '%s' % (dict.__repr__(self))

    def __missing__(self, key):
        if self.default:
            return self.default(key)
        else:
            return self.exception_fun()

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)


class MyRecursiveDefDict(MyDefaultdict):

    def __getitem__(self, key):
        if key in self: return self.get(key)
        return self.setdefault(key, MyRecursiveDefDict())

    def __repr__(self):
        if key in self: return self.__repr__(key)
        return str(self.default, dict.__repr__(self))


if __name__ == "__main__":
    d = MyDefaultdict()
    d['a']='a'
    d['v'] = 'v'
    print(str(d))
    print(d['d'])

    nums = MyRecursiveDefDict()
    nums[1][2] = 5
    print(nums[1][2] == 5)
