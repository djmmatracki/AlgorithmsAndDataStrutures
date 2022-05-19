import time
import random


# def insertion_sort(array):
#     n = len(array)
#     i = 1
#     while i < n:
#         key = array.pop(i)
#         placed = False
#         j = i - 1
#         while j >= 0:
#             if array[j] > key:
#                 j -= 1
#                 continue
            
#             array.insert(j+1, key)
#             placed = True
#             break

#         if not placed:
#             array.insert(0, key)
#         i += 1


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def shell_sort(array):
    h = len(array) // 2
    n = len(array)

    while h > 0:
        i = 0
        j = h
        while j < n:
            if array[i] > array[j]:
                swap(array, i, j)
            i += 1
            j += 1

            k = i
            while k - h >= 0:
                if array[k] < array[k-h]:
                    swap(array, k, k-h)
                k -= 1
        h //= 2
    

def quicksort(array, start, end):
    if start >= end:
        return

    middle = (end + start) // 2
    pivot = array[middle]
    i = start
    j = end

    while i < j:
        while array[i] < pivot:
            i += 1
        
        while array[j] > pivot:
            j -= 1
        
        if i < j:
            swap(array, i, j)
            i += 1
            j -= 1

    if start < j:
        quicksort(array, start, j)

    if end > i+1:
        quicksort(array, i, end)


if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(10000)]
    t_start = time.perf_counter()
    shell_sort(arr)
    t_stop = time.perf_counter()

    print("Czas obliczeń sortowania shell sort dla duzej tablicy:", "{:.7f}".format(t_stop - t_start)) 
    print()


    arr = [random.randint(0, 100) for _ in range(10000)]
    t_start = time.perf_counter()
    quicksort(arr, 0, len(arr)-1)
    t_stop = time.perf_counter()

    print("Czas obliczeń sortowania quick sort dla duzej tablicy:", "{:.7f}".format(t_stop - t_start))
    print()