from memory_profiler import profile

from time import time


def timing(f):
    @warps(f)
    def warp(*args, **kw):
        ts = time()
        result = f(*args, *kw)
        te = time()
        print('func:%r args:[%r, %r] took: % 2.4f fec' %(f.__name__, args, kw, te-ts))
        return result
    return warp


def pickline(file_obj, pos):
    file_obj.seek(pos)
    return file_obj.readline()

def merge_sort_local(array: list) -> list:
    arr_len = len(array)
    if arr_len == 1 or arr_len == 0:
        return array
    left, rigth = array[:arr_len//2], array[arr_len//2:]
    merge_sort_local(left)
    merge_sort_local(rigth)
    n=m=k=0
    new_arr = [0]* arr_len
    while n < len(left) and m < len(rigth):
        if left[n]<= rigth[m]:
            new_arr[k] = left[n]
            n+=1
        else:
            new_arr[k] = rigth[m]
            m+=1
        k += 1
    while n < len(left):
        new_arr[k] = left[n]
        n += 1
    while m < len(rigth):
        new_arr[k] = rigth[m]
        m += 1


def merge_sort_global(array: list, positions: list, file_obj) -> list:
    arr_len = len(array)
    if arr_len == 1 or arr_len == 0:
        return array
    left, rigth = array[:arr_len // 2], array[arr_len // 2:]
    merge_sort_global(left, positions, file_obj)
    merge_sort_global(rigth, positions, file_obj)
    n = m = k = 0
    new_arr = [0] * arr_len
    while n < len(left) and m < len(rigth):
        row_left = pickline(file_obj, positions[left[n]])
        row_rigth = pickline(file_obj, positions[rigth[n]])
        if row_left <= row_rigth:
            new_arr[k] = left[n]
            n+=1
        else:
            new_arr[k] = rigth[m]
            m+=1
        k += 1
    while n < len(left):
        new_arr[k] = left[n]
        n+= 1


@profile
def file_sort(filename_in: str):
    positions = []  # type List[int]
    filename, extension = filename_in.rsplit('.',1)
    filename_tmp = filename + '_tmp.' + extension
    filename_out = filename + '_out.' + extension

    print(f'>>>>creating temporary file {filename_tmp} with sorted words in each line')
    with open(filename_in, mode='r') as file_in:
        with open(filename_tmp, mode='w', newline='\n') as file_out:
            previous_pos = 0
            row = file_in.readline()
            while row:
                positions.append(previous_pos)
                previous_pos = file_in.tell()
                row_words = row.split()
                merge_sort_local(row_words)
                file_out.write(' '.join(row_words) + '\n')
                row = file_in.readline()
            temp_array = list(range(len(positions)))

    print('>>> Sorting lines >>>')
    with open(filename_tmp, mode='r') as tmp_file:
        merge_sort_global(temp_array, positions, tmp_file)
        print(f'>>>Creating output file {filename_out}')
        with open(filename_out, mode='w', newline='\n') as out_file:
            for i in temp_array:
                cur_row = pickline(tmp_file, positions[i]).strip()
                out_file.write(cur_row + '\n')


if __name__ == '__main__':
    print(file_sort('test.txt'))