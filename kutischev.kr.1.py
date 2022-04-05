def iterator(fill=0, *args):
    max = len(args[0])
    for i in args:
        if len(i)>max:
            max = len(i)

    array = []
    for i in range(len(args)):
        array +=[[0]*max]
#    array = [[0]*max]*len(args)
#    array = array[:]

    for i in range(0,len(args)):

        l = len(args[i])-1
        for j in range(len(args[i])):
            if j > l:
                array[i][j]=fill
            else:
                array[i][j] = args[i][j]
            print(array)

    lst = []
    for i in range(max):
        lst += [[0] * len(args)]
    for i in array:
        print(i)
        for j in array: pass

    print(lst)

two = [5, 2, 3, "l"]
one = ['h', 'd', 's','d', 5]
fil = 0
gen = iterator(fil, one, two)



