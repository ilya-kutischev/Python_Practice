import os


def read_words(filename):
    with open(filename, 'r', encoding='utf8') as f:
        while True:
            buf = f.read(10240)
            if not buf:
                break
            while not str.isspace(buf[-1]):
                ch = f.read(1)
                if not ch:
                    break
                buf += ch
            words = buf.split()
            for word in words:
                yield word.lower()
        yield '' # в конце оставим пустую строку для определения конца файла


def search_words(filename, frag: str):
    l = len(frag)
    frag.lower()
    temp_filename = frag + '_temp.txt'
    with open(temp_filename, 'w') as f:
        for word in read_words(filename):
            word.lower()
            if frag == word[:l].lower():
                f.write(word + '\n')


def count_words_with(filename, frag: str):
    frag = frag.lower()
    search_words(filename, frag)
    lines = 0
    temp_filename = frag + '_temp.txt'
    with open(temp_filename) as f:
        for line in f:
            lines = lines + 1
    try:
        os.remove(temp_filename)
    except OSError:
        pass
    return lines


def find_starting_letters(filename):
    letters = []
    for word in read_words(filename):
        if word == '':
            break
        if word[0].lower() in letters:
            pass
        else:
            letters += [word[0].lower()]
    return letters


def made_tree(filename):
    letters = find_starting_letters(filename)
    st = '|--'
    count = 0
    for i in letters:
        i = i.lower()
        n = count_words_with(filename, i)
        print(st + ' ' + i + ' ' + str(n))
        if count < len(letters)//2:
            st = '| ' + st
        else:
            st = st[2:]
        count += 1


if __name__ == '__main__':
    print(count_words_with('file.txt', 'аб'))
    print(made_tree('file.txt'))