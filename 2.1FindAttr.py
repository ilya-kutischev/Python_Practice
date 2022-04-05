class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class SimpleClass:
    pass


def stupid_function(num):
    stupid_function.a = num

    return stupid_function


def find_attribute_v1(num, obj):
    """searching value in list of attributes by using getattr"""
    d = dir(obj)
    for i in d:
        if num == obj.__getattribute__(i):
            return i


def find_attribute_v2(num, obj):
    """searching value in dict with attributes and values"""
    d = obj.__dict__
    for v in d.items():
        if num == v[1]:
            return v[0]


if __name__ == '__main__':
    object = MyClass(1, 2, 3)
    print('This value has attribute: ', find_attribute_v1(1, object))
    print('This value has attribute: ', find_attribute_v2(3, object))
    x = SimpleClass()
    x.a = 1
    x.b = 2
    x.c = 3
    print('This value has attribute: ', find_attribute_v2(2, x), ' ', find_attribute_v2(2, x) == 'b')
    print('This value has attribute: ', find_attribute_v1(3, x), ' ', find_attribute_v2(3, x) == 'c')
    print('This value has attribute: ', find_attribute_v1(5, stupid_function(5)), ' ',
          find_attribute_v2(5, stupid_function(5)) == 'a')