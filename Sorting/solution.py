

class Element:
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority = priority
    
    def __gt__(self, other):
        return self.priority > other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    
    def __eq__(self, __o: object) -> bool:
        return self.priority == __o.priority
    
    def __str__(self) -> str:
        return f"{self.value} : {self.priority}"


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
        i = self.parent(self.size - 1)

        while i >= 0:
            current = i
            while current < len(array):
                leftIndex = self.left(current)
                rightIndex = self.right(current)

                if rightIndex >= len(array):
                    break
                

                if array[leftIndex] > array[current]:
                    array[current], array[leftIndex] = array[leftIndex], array[current]
                    current = leftIndex
                    continue

                if array[rightIndex] > array[current]:
                    array[current], array[rightIndex] = array[rightIndex], array[current]
                    current = rightIndex
                    continue

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
                array[current], array[leftIndex] = array[leftIndex], array[current]
                current = leftIndex
                continue

            if array[rightIndex] > array[current]:
                array[current], array[rightIndex] = array[rightIndex], array[current]
                current = rightIndex
                continue


    def sort(self, array):
        # Utworzenie kopca z tablicy
        if len(array) == 0:
            return

        self.array2heap(array)

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


def swap_selection_sort(array):
    n = len(array)
    i = 0

    while i < n:
        m = argmin(arr[i:]) + i
        swap(arr, i, m)
        i += 1


def shift(array):
    pass


def shift_selection_sort(array):
    n = len(array)
    i = 0

    while i < n:
        m = argmin(arr[i:]) + i
        swap(arr, i, m)
        i += 1


if __name__ == "__main__":
    heap_sort = HeapSort()
    arr = [9, 2, 7, 6, 0, 1, 5]
    # heap_sort.sort(arr)
    swap_selection_sort(arr)
    print(arr)