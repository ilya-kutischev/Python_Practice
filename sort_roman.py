import linecache


# from memory_profiler import profile


def comp(lhs, rhs, file):
    if isinstance(rhs, int):
        return get_current_line(file, lhs) <= get_current_line(file, rhs)
    else:
        return lhs <= rhs


def merge_sort(my_list, file):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    left_list = my_list[:mid]
    right_list = my_list[mid:]

    merge_sort(left_list, file)
    merge_sort(right_list, file)

    index_left = index_right = index_main = 0

    while index_left < len(left_list) and index_right < len(right_list):
        if comp(right_list[index_right], left_list[index_left], file):
            my_list[index_main] = right_list[index_right]
            index_right += 1
        else:
            my_list[index_main] = left_list[index_left]
            index_left += 1
        index_main += 1

    while index_left < len(left_list):
        my_list[index_main] = left_list[index_left]
        index_left += 1
        index_main += 1

    while index_right < len(right_list):
        my_list[index_main] = right_list[index_right]
        index_right += 1
        index_main += 1


def get_positions(file):
    yield 0
    while file.readline():
        yield file.tell()


def get_current_line(file, pos):
    file.seek(pos)
    return file.readline()


# @profile
def file_sort(filename):
    name, ext = filename.rsplit('.')
    global temp_filename
    temp_filename = name + '_temp.' + ext
    out_filename = name + '_out.' + ext

    with open(filename, "r") as file:
        with open(temp_filename, "w") as temp_file:
            for line in file:
                merge_sort(sorted_line := line.split(), temp_file)
                temp_file.write(' '.join(sorted_line) + '\n')

    with open(temp_filename, "r") as temp_file:
        with open(out_filename, "w", newline="\n") as out_file:
            size = list(get_positions(temp_file))
            merge_sort(size, temp_file)
            for num in size:
                out_file.write(get_current_line(temp_file, num))


file_sort("test.txt")