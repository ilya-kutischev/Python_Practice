#задан список, нужно найти число в списке и всё до него удалить
def delete_before(items: list, border: int)-> list:
    if len(items) == 0 or items.count(border) == 0:
        return items
    else:
        return items[items.index(border):]

def delete_before1(items: list, border: int)-> list:
    try:
        return items[items.index(border):]
    except ValueError:  #exceptions errors
        return items




if __name__ == '__main__':
    print(delete_before([1,2,3,4,5,6,7,8,9],8))
    print(delete_before([1,2,3,4,5,6,7,8,9],10))
    print(delete_before([],8))
    
    print(delete_before1([1,2,3,4,5,6,7,8,9],8))
    print(delete_before1([1,2,3,4,5,6,7,8,9],10))
    print(delete_before1([],8))