import time
import random


class Element:
    def __init__(self, key, priority) -> None:
        self.value = key
        self.priority = priority
    
    def __str__(self) -> str:
        return f"{self.value} - {self.priority}"

    def __repr__(self) -> str:
        return f"{self.value} - {self.priority}"
    
    def __gt__(self, other):
        return self.priority > other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __eq__(self, __o: object) -> bool:
        return self.priority == __o.priority
    

class HeapSort:

    def __init__(self) -> None:
        pass

    def parent(self, index):
        """Returns index of parent node"""
        return (index - 1) // 2

    def left(self, index):
        """Returns index of left node"""
        return index * 2 + 1

    def right(self, index):
        """Returns index of right node"""
        return index * 2 + 2

    def array2heap(self, array):
        i = self.parent(len(array)-1)

        while i >= 0:
            current = i
            while current < len(array):
                leftIndex = self.left(current)
                rightIndex = self.right(current)

                if rightIndex >= len(array):
                    break

                if array[leftIndex] > array[current]:
                    if array[leftIndex] >= array[rightIndex]:
                        array[current], array[leftIndex] = array[leftIndex], array[current]
                        current = leftIndex
                        continue

                if array[rightIndex] > array[current]:
                    if array[leftIndex] <= array[rightIndex]:
                        array[current], array[rightIndex] = array[rightIndex], array[current]
                        current = rightIndex
                        continue

                break

            i -= 1
        
    
    def virtual_dequeue(self, array, size):
        current = 0
        array[current], array[size - 1] = array[size - 1], array[current]
        size -= 1

        while current < size:
            leftIndex = self.left(current)
            rightIndex = self.right(current)
            
            if rightIndex >= size:
                break

            if array[leftIndex] > array[current]:
                if array[leftIndex] >= array[rightIndex]:
                    array[current], array[leftIndex] = array[leftIndex], array[current]
                    current = leftIndex
                    continue

            if array[rightIndex] > array[current]:
                if array[leftIndex] <= array[rightIndex]:
                    array[current], array[rightIndex] = array[rightIndex], array[current]
                    current = rightIndex
                    continue

            break

    def print_tab(self, array):
        n = len(array)

        print ('{', end=' ')
        if n > 0:
            for i in range(n-1):
                print(array[i], end = ', ')
            if array[n-1]: print(array[n-1] , end = ' ')
        print( '}')

    def print_tree(self, idx, lvl, array):
        if idx < len(array):
            self.print_tree(self.right(idx), lvl+1, array)
            print(2*lvl*'  ', array[idx] if array[idx] else None)            
            self.print_tree(self.left(idx), lvl+1, array)


    def sort(self, array, show=False):
        # Utworzenie kopca z tablicy
        if len(array) == 0:
            return

        self.array2heap(array)

        if show:
            self.print_tab(array)
            self.print_tree(0, 0, array)

        size = len(array)
        i = size
        while i > 0:
            self.virtual_dequeue(array, i)
            i -= 1
    

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def argmin(arr):
    if len(arr) == 0:
        return
    arg = 0
    minimal = arr[arg]
    for i, el in enumerate(arr):
        if el < minimal:
            arg = i
            minimal = el
    return arg


def selection_sort(array):
    n = len(array)
    i = 0

    while i < n:
        m = argmin(arr[i:]) + i
        swap(arr, i, m)
        i += 1


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


if __name__ == "__main__":
    arr = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    arr = [Element(key, value) for value, key in arr]
    heap_sort = HeapSort()

    heap_sort.sort(arr, show=True)
    # Algorytm nie jest stabilny
    heap_sort.print_tab(arr)

    arr = [random.randint(0, 100) for _ in range(10000)]
    t_start = time.perf_counter()
    heap_sort.sort(arr)
    t_stop = time.perf_counter()
    print("Czas obliczeń sortowania kopcowego dla duzej tablicy:", "{:.7f}".format(t_stop - t_start)) 

    print()
    print("=================================================")
    print()

    arr = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    arr = [Element(key, value) for value, key in arr]
    selection_sort(arr)
    print("Wynik sortowania insertion sort")
    print(arr)
    
    arr = [random.randint(0, 100) for _ in range(10000)]
    t_start = time.perf_counter()
    selection_sort(arr)
    t_stop = time.perf_counter()
    print("Czas obliczeń sortowania insertion sort dla duzej tablicy:", "{:.7f}".format(t_stop - t_start))

    print()
    print("=================================================")
    print()

    arr = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    arr = [Element(key, value) for value, key in arr]
    insertion_sort(arr)
    print("Wynik sortowania insertion sort")
    print(arr)
    
    arr = [random.randint(0, 100) for _ in range(10000)]
    t_start = time.perf_counter()
    insertion_sort(arr)
    t_stop = time.perf_counter()
    print("Czas obliczeń sortowania insertion sort dla duzej tablicy:", "{:.7f}".format(t_stop - t_start))

    print()
    print("=================================================")
    print()
