def flatten_it(obj):
    """Recursive flatten function"""
    if not isinstance(obj, str) and hasattr(obj, '__iter__'):
        for el in obj:
            if el != obj:
                yield from flatten_it(el)
            else:
                raise ValueError
    else:
        yield obj


if __name__ == "__main__":
    # Test 1

    print(list(flatten_it([1, "21321", [1, [2, [2, [3, 4]]]]])))

    # Test 2
    try:
        a = [1, 2]
        a[1] = a
        print(list(flatten_it([1, a, (3, 4, 5), [6, [7, 8]]])))
    except ValueError:
        print("Self-referenced list")

    # Test 3

    b = map(int, ["2", "3"])
    print(list(flatten_it([1, {1, 2, 3}, ("dsa", 2, b)])))

    # Test 4

    print(list(flatten_it([1, 2, [({x: x ** 2 for x in range(10)})], {1, "23", 3}])))

    # Test 5

    print(list(flatten_it(((((((1, [2, 4 * [{2, 4}]], "fgddsa", flatten_it([1, [2, 4], 3]))))))))))