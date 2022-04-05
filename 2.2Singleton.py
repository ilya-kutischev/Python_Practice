def singleton(class_):
    """We use a decorator to make a singleton"""
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton  # using decorator
class MyClass():  # example class
    pass


class Singleton2Base(type):
    _instances = {}
    """Making a singleton by using metaclass"""

    def __call__(cls, *args, **kwargs):  # calling of obj like a function
        if cls not in cls._instances:  # comparing
            cls._instances[cls] = super(Singleton2Base, cls).__call__(*args, **kwargs)  # adding new argument
        return cls._instances[cls]


class Singleton2(metaclass=Singleton2Base):  # using metaclass
    def __init__(self):  # function for initialization
        self.a = 0

    def set_a(self, n):  # setting some arguments
        self.a = n

    def get_a(self):  # getting argument's value
        return self.a


if __name__ == '__main__':  # checking of results
    x = MyClass()  # first example
    y = MyClass()
    x.a = 5
    print(x.a == y.a)

    s = Singleton2()  # second example
    r = Singleton2()
    r.set_a(5)
    print(s.a == r.a)