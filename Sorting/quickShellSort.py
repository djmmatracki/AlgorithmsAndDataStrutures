import time
import random
from unittest import result
import numpy as np


def insertion_sort(array):
    n = len(array)
    i = 1
    while i < n:
        key = array.pop(i)
        placed = False
        j = i - 1
        while j >= 0:
            if array[j] > key:
                j -= 1
                continue
            
            array.insert(j+1, key)
            placed = True
            break

        if not placed:
            array.insert(0, key)
        i += 1


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def shell_sort(array):
    n = len(array)
    k = 0

    while (3**k - 1) / 2 < n // 3:
        k += 1
        break
    k -= 1
    h = int((3**k - 1) / 2)

    while h > 0:
        j = h
        while j < n:
            i = j - h
            while i >= 0:
                if array[i+h] > array[i]:
                    break
                else:
                    swap(array, i, i+h)
                i -= h
            j += 1
        h //= 3

def median_2(a, b):
    return (a + b) // 2

def median_3(a, b, c):
    return max(min(a,b), min(c,max(a,b)))

def median_4(a, b, c, d):
    f = max(min(a,b), min(c,d))
    g = min(max(a,b), max(c,d))
    return median_2(f, g)

def median_5(a, b, c, d, e):
    f = max(min(a,b), min(c,d))
    g = min(max(a,b), max(c,d))
    return median_3(e,f,g)

def magicFive(array):
    result = []
    i = 0
    while i < len(array):
        tab = array[i:i+5]
        if len(tab) == 5:
            result.append(median_5(tab[0], tab[1], tab[2], tab[3], tab[4]))
        elif len(tab) == 4:
            result.append(median_4(tab[0], tab[1], tab[2], tab[3]))
        elif len(tab) == 3:
            result.append(median_3(tab[0], tab[1], tab[2]))
        elif len(tab) == 2:
            result.append(median_2(tab[0], tab[1]))
        else:
            result.append(tab[0])

        i += 5

    if len(result) == 1:
        return result[0]
    
    return magicFive(result)

def quicksort(array, magic_five=False):
    if len(array) < 2:
        return array

    if magic_five:
        pivot = magicFive(array)
    else:
        pivot = array[0]
    less = []
    greater = []
    equal = []

    for el in array:
        if el < pivot:
            less.append(el)
        elif el > pivot:
            greater.append(el)
        else:
            equal.append(el)

    return quicksort(less, magic_five) + equal + quicksort(greater, magic_five)


if __name__ == "__main__":
    arr1 = [random.randint(0, 100) for _ in range(10000)]
    arr2 = [random.randint(0, 100) for _ in range(10000)]

    t1 = time.perf_counter()
    shell_sort(arr1)
    t2 = time.perf_counter()
    insertion_sort(arr2)
    t3 = time.perf_counter()

    print("Czas obliczeń sortowania shell sort dla duzej tablicy:", "{:.7f}".format(t2 - t1)) 
    print("Czas obliczeń sortowania insertion sort dla duzej tablicy:", "{:.7f}".format(t3 - t2)) 
    print()


    arr1 = [random.randint(0, 100) for _ in range(10000)]

    t1 = time.perf_counter()
    result1 = quicksort(arr1, magic_five=True)
    t2 = time.perf_counter()
    result2 = quicksort(arr1, magic_five=False)
    t3 = time.perf_counter()

    print("Czas obliczeń sortowania quick sort dla duzej tablicy dla magicznych piatek:", "{:.7f}".format(t2 - t1))
    print("Czas obliczeń sortowania quick sort dla duzej tablicy bez magicznych piatek:", "{:.7f}".format(t3 - t2))
    print("Czy uzyskano identyczne rezultaty", result1 == result2 and result1 == sorted(arr1))
    print()
