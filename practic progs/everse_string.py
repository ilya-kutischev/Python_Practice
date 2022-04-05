#набор строк разделен пробедами, вернуть все слова развернутыми в обратном порядке
#.split(' ') делит на строки по пробелам
def get_reverse_words(text: str)-> str:
    return ' '.join([word[::-1] for word in text.split(' ')])

if __name__ == '__main__':
    print(get_reverse_words('hello world'))