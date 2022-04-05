import sys
import random
import time
import copy


def python_sort(lst, out = True):
    print('\npython sort')
    arr = copy.deepcopy(lst)
    t0 = time.time()
    arr.sort()
    print(time.time()-t0)
    if out:
        print(arr)


def selection_sort(lst, out = True):
    print('\nselection sort')
    arr = copy.deepcopy(lst)
    t0 = time.time()
    n = len(arr)
    for i in range(n):
        m=i
        for j in range(i+1,n):
            if(arr[m]>arr[j]):
                m=j
        arr[i], arr[m] = arr[m], arr[i]
    print(time.time()-t0)
    if out:
            print(arr)


def bubble_sort(lst, out = True):
    print('\nbubble sort')
    arr = copy.deepcopy(lst)
    t0 = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(time.time()-t0)
    if out:
        print(arr)


def insertion_sort(lst, out = True):
    print('\n insertion sort')
    arr = copy.deepcopy(lst)
    t0 = time.time()
    n = len(arr)
    for i in range(1, n):
        j = i
        while (j>0 and arr[j-1]>arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1
    print(time.time()-t0)
    if out:
        print(arr)


def quick_sort(lst, out = True):
    print('\nquick sort')
    arr = copy.deepcopy(lst)

    def partition(lst, left, rigth):
        pivot = lst[rigth]
        i = left-1
        for j in range(left, rigth):
            if lst[j]<pivot:
                i+=1
                lst[i], lst[j]= lst[j], lst[i]
        lst[i+1], lst[rigth]= lst[rigth], lst[i+1]
        return i+1

    def quicksort(lst, left, rigth):
        if left<rigth:
            p = partition(lst, left, rigth)
            quicksort(lst, left, p-1)
            quicksort(lst, p+1, rigth)
    t0 = time.time()
    n = len(arr)
    quicksort(arr, 0, n-1)
    print(time.time()-t0)
    if out:
        print(arr)


def merge_sort(lst, out = True):
    print('\nmerge sort')

    def merge(lst, left, rigth, mid):
        a = lst[left:mid+1]
        b = lst[mid+1:rigth+1]

        i = 0
        j = 0
        k = left
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                lst[k] = a[i]
                i += 1
            else:
                lst[k] = b[j]
                j = j+1
            k = k+1
        while i < len(a):
            lst[k] = a[i]
            i = i+1
            k +=1
        while j < len(b):
            lst[k] = b[j]
            j +=1
            k += 1

    def merge_sorting(lst, left, rigth):
        if left < rigth:
            mid = left+(rigth-left)//2
            merge_sorting(lst, left, mid)
            merge_sorting(lst, mid+1, rigth)
            merge(lst, left, rigth, mid)
    t0 = time.time()
    arr = copy.deepcopy(lst)
    merge_sorting(arr, 0, len(arr)-1)
    print(time.time() - t0)
    if out:
        print(arr)


numbers = [random.randrange(1000) for x in range(int(sys.argv[1]))]
out = False
if len(sys.argv) > 2:
    out = bool(sys.argv[2])
sys.setrecursionlimit(150000)

python_sort(numbers, out)
quick_sort(numbers, out)
merge_sort(numbers, out)
selection_sort(numbers, out)
insertion_sort(numbers, out)
bubble_sort(numbers, out)

