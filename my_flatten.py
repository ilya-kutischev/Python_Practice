def flatten_it(data):
    if isinstance(data, dict):
        flatten_dict = []
        for k, v in data.items():
            if v == data:
                raise ValueError('Cyclic reference')
            else:
                flatten_dict.extend((k, v))
        for i in flatten_it(flatten_dict):
            yield i
    elif hasattr(data, '__iter__') and not isinstance(data, str):
        for i in data:
            if i == data:
                raise ValueError('Cyclic reference')
            for j in flatten_it(i):
                yield j
    else:
        yield data



if __name__ == "__main__":
    print(list(flatten_it([1, 2, [3, 4, ('five', {'6': 'six'})]])))
    print(list(flatten_it((1, {'2': [3, [4, [5, (6, "seven")]]]}))))
    lst = [0, 0]
    lst[1] = lst
    print(list(flatten_it(lst)))