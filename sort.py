import sys
import os


def sort_splited_file(file_name):
    folder_list = os.listdir(path='temp' + ' ' + file_name)
    for folder in folder_list:
        folder_path = 'temp' + ' ' + file_name + '/' + folder
        file_list = os.listdir(path=folder_path)
        sorted_words = sort_words(folder_path, file_list)
        for i in range(len(sorted_words)):
            os.rename(folder_path + '/' + sorted_words[i], folder_path + '/' + str(i) + 'srt')
    folders_path = 'temp' + ' ' + file_name
    sorted_strings = sort_strings(folders_path, folder_list)
    for i in range(len(sorted_strings)):
        os.rename(folders_path + '/' + sorted_strings[i], folders_path + '/' + str(i) + 'srt')


def split_file(file_name):
    split_on_strings(file_name)
    file_list = os.listdir(path='temp' + ' ' + file_name)
    split_on_words(file_name,file_list)


def split_on_strings(file_name):
    split_path = 'temp' + ' ' + file_name
    os.mkdir(split_path)
    file_num = 0
    with open(file_name, 'r', encoding = 'utf-8' ) as file:
        new_file = open (split_path + '/' + str(file_num), 'w', encoding = 'utf-8')
        while True:
            char = file.read(1)
            if char == '':
                break
            if char != '\n': 
                new_file.write(char)
            else:
                new_file.close()
                file_num +=1
                new_file = open (split_path + '/' + str(file_num), 'w', encoding = 'utf-8')
        new_file.close()


def split_on_words(file_name, file_list):
    cur_dir = 'temp' + ' ' + file_name
    for file in file_list:
        with open(cur_dir + '/' + file, 'r', encoding = 'utf-8') as string:
            os.mkdir(cur_dir + '/' + file + 'str')
            file_num = 0
            new_file = open(cur_dir + '/' + file  + 'str' + '/' + str(file_num), 'w', encoding = 'utf-8')
            while True:
                char = string.read(1)
                if char == '' or char == '\n':
                    break
                elif char == ' ':
                    new_file.close()
                    file_num += 1
                    new_file = open(cur_dir + '/' + file  + 'str' + '/' + str(file_num), 'w', encoding = 'utf-8')
                else:
                    new_file.write(char)
            new_file.close()
        os.remove(cur_dir + '/' + file)


def merge_words(a,b,folder_path):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        file_1 = open(folder_path + '/' + a[i], 'r', encoding='utf-8')
        file_2 = open(folder_path + '/' + b[j], 'r', encoding='utf-8')
        first_word = file_1.read()
        second_word = file_2.read()
        if first_word > second_word:
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1
        file_1.close()
        file_2.close()
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def sort_words(folder_path, file_list):
    if len(file_list) == 1:
        return file_list
    middle = len(file_list) // 2
    left = sort_words(folder_path,file_list[:middle])
    right = sort_words(folder_path,file_list[middle:])
    return merge_words(left,right,folder_path)


def sort_strings(folders_path, folder_list):
    if len(folder_list) == 1:
        return folder_list
    middle = len(folder_list) // 2
    left = sort_strings(folders_path,folder_list[:middle])
    right = sort_strings(folders_path,folder_list[middle:])
    return merge_strings(left,right,folders_path)


def merge_strings(a,b,folders_path):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        first_files_list = os.listdir(path=folders_path + '/' + a[i])
        second_files_list = os.listdir(path=folders_path + '/' + b[i])
        first_amount_files = len(first_files_list)
        second_amount_files = len(second_files_list)
        for k in range(min(first_amount_files, second_amount_files)):
            file_1 = open(folders_path + '/' + a[i] + '/' + str(k) + 'srt', 'r', encoding='utf-8')
            file_2 = open(folders_path + '/' + b[j] + '/' + str(k) + 'srt', 'r', encoding='utf-8')
            first_word = file_1.read()
            second_word = file_2.read()
            file_1.close()
            file_2.close()    
            if first_word > second_word:
                c.append(b[j])
                j+=1
                break
            elif second_word > first_word:
                c.append(a[i])
                i+=1
                break
            else:
                continue
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def build_file(file_name, result_file_name):
    with open(result_file_name, 'w', encoding = 'utf-8' ) as result_file:
        folders_list = os.listdir(path='temp' + ' ' + file_name)
        for folder in folders_list:
            files_list = os.listdir(path='temp' + ' ' + file_name + '/' + folder)
            for file in files_list:
                with open('temp' + ' ' + file_name + '/' + folder + '/' + file, 'r', encoding='utf-8') as reading_file:
                    while True:
                        char = reading_file.read(1)
                        if char != '' and char != '\n':
                            result_file.write(char)
                        else:
                            break
                os.remove('temp' + ' ' + file_name + '/' + folder + '/' + file)
                if file != files_list[-1]:
                    result_file.write(' ')
            os.rmdir('temp' + ' ' + file_name + '/' + folder)
            if folder != folders_list[-1]:
                result_file.write('\n')
    os.rmdir('temp' + ' ' + file_name)

def sort_file(file_name, result_file_name):
    split_file(file_name)
    sort_splited_file(file_name)
    build_file(file_name, result_file_name)

if __name__ == '__main__':
    args_amount = len(sys.argv)
    if args_amount == 1:
        file_name = input('Enter name of file:')
        result_file_name = input('Enter name of result file:')
    elif args_amount == 2:
        file_name = result_file_name = sys.argv[1]
    else:
        file_name = sys.argv[1]
        result_file_name = sys.argv[2]
    sort_file(file_name, result_file_name)