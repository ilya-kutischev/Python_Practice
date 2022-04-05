# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def flatten_it(it):
    if isinstance(it, dict):
        flatten_dict = []
        for k, v in it.items():
            if v == it:
                raise ValueError('Cyclic reference detected')
            else:
                flatten_dict.extend((k, v))
        for elem_2 in flatten_it(flatten_dict):
            yield elem_2
    elif hasattr(it, '__iter__') and not isinstance(it, str):
        for elem in it:
            if elem == it:
                raise ValueError('Cyclic reference detected')
            else:
                for elem_2 in flatten_it(elem):
                    yield elem_2
    else:
        yield it


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_1 = [1, 2]
    list_1[0] = list_1

    test_list = [
        1,
        [1, 2, [3, 4], (5, 6, 7)],
        "123",
        [1, 2, 3],
        [2, {1: 3, 2: 5}]]

    for elem in test_list:
        print(f'before: {elem}')
        print(f'after: {list(flatten_it(elem))}')