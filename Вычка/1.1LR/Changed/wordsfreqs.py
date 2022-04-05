import sys
import string
import codecs

filename = sys.argv[1]
length = sys.argv[2]
tab = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # удаляем пунктуацию
text = ""
with codecs.open(filename, "r", "utf-8" ) as file:
    text = file.read()
splited_text = text.translate(tab).lower().split()
word_lists = []
fl = 0
for word in splited_text:
    for lst in word_lists:
        if lst[0] == word:
            lst[1] += 1
            fl = 1
    if fl == 0:
        word_lists.append([word, 1])
    fl = 0
    i = 0
while not len(word_lists) == i + 1:
    if len(word_lists[i][0]) < length:
        del word_lists[i]
        i -= 1
    i += 1

word_lists.sort(key=lambda i: i[1], reverse=True)
for i in range(20):
    print(f'#{i}    {word_lists[i][0]}      {word_lists[i][1]}')
