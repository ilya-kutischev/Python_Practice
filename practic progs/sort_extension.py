#
from os import listdir
FILE_LIST = listdir('C:\\Users\\admin\\Desktop\\folder')

def find_extention(filename: str) -> str:
    if filename.startswith('.') == True and filename.count('.') == 1:
        return ''
    else:
        return filename[filename.rfind('.') + 1:]

def find_name(filename: str) -> str:
    if filename.startswith('.') == True and filename.count('.') == 1:
        return filename
    else:
        return filename[:filename.rfind('.')]
    
def sort_by_extention(files: list)-> list:
     files.sort(key = lambda x: (find_extention(x), find_name(x)))
     return files

if __name__ == '__main__':
    print(sort_by_extention(FILE_LIST))