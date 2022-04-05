import sys
import string
import codecs

filename = sys.argv[1]
with open(filename, "r") as file:
    text = file.readlines()
print(text)
non_repeated = set(text)
print(non_repeated)
with open(filename, "w") as file:
    file.writelines(non_repeated)