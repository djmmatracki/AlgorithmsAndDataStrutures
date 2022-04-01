
STATIC_LIST_LENGTH = 6

def addElementAtIndex(array, index, val):
    i = index
    prev = array[i]
    array[i] = val
    i += 1

    while i < len(array):
        if array[i] is None:
            array[i] = prev
            break

        last = array[i]
        array[i] = prev
        prev = last
        i += 1


def addElementAtEnd(array, val):
    i = 0
    while array[i] is None:
        i += 1
        if i == len(array):
            return
    array[i] = val


class Node:
    def __init__(self, data=None, next=None) -> None:
        if data is None:
            self.data = [None for _ in range(STATIC_LIST_LENGTH)]
        else:
            self.data = data

        self.next = next

    @property
    def size(self):
        size = 0
        i = 0
        while i < len(self.data):
            if self.data[i] is not None:
                size += 1
            i += 1
        return size

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == STATIC_LIST_LENGTH

    
class UnrolledLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def destroy(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None
    
    def length(self) -> int:
        current = self.head
        lenght = 0
        while current is not None:
            current = current.next
            lenght += 1

        return lenght * STATIC_LIST_LENGTH
    
    def get(self, index):
        nodeIndex = (index // STATIC_LIST_LENGTH)
        i = 0
        current = self.head

        if current is None:
            return None

        while i < nodeIndex:
            current = current.next
            i += 1
        staticListIndex = index % STATIC_LIST_LENGTH

        return current.data[staticListIndex]
    

    def insert(self, index, val):
        current = self.head

        # Jezli lista jest pusta
        if current is None:
            newList = [None for _ in range(STATIC_LIST_LENGTH)]
            newList[0] = val
            self.head = Node(data=newList)
            return
        # -----

        nodeIndex = (index // STATIC_LIST_LENGTH)
        i = 0

        # Szukamy node'a do ktorego mamy dodac element
        while i < nodeIndex:
            beforeCurrent = current
            current = current.next
            i += 1
        # -----
        
        # Indeks jest poza tablica wiec musimy dodac na koniec
        if current is None:
            if beforeCurrent.data[-1] is not None:
                newList = [None for _ in range(STATIC_LIST_LENGTH)]
                newList[0] = val
                beforeCurrent.next = Node(data=newList)
                return
            
            beforeCurrent.data[-1] = val
            return
        # ------

        staticListIndex = index % STATIC_LIST_LENGTH

        # Jezeli index jest pusty wstawiamy element
        if current.data[staticListIndex] is None:
            current.data[staticListIndex] = val
            return
        # -------


        # Jezeli index jest zajety ale tablica nie jest pelna
        if not current.isFull():
            addElementAtIndex(current.data, staticListIndex, val)
            return

        # ------
        # Jezeli tablica jest pelna
        
        # Patrzymy w ktorej polowej jest index
        mid = STATIC_LIST_LENGTH // 2
        left = current.data[:mid] + [None for _ in range(mid)]
        right =  current.data[mid:] + [None for _ in range(mid)]

        if staticListIndex >= mid:
            left[staticListIndex] = val
        else:
            addElementAtIndex(left, staticListIndex, val)

        current.data = left
        nextNode = current.next
        newNode = Node(data=right)
        newNode.next = nextNode
        current.next = newNode

        return
    

    def remove(self, index):
        current = self.head

        if current is None:
            return

        nodeIndex = (index // STATIC_LIST_LENGTH)
        i = 0

        # Szukamy node'a od ktorego mamy usunac
        while i < nodeIndex:
            current = current.next
            i += 1

        if current is None:
            return

        staticListIndex = index % STATIC_LIST_LENGTH

        # Sprawdzamy czy element jest juz pusty
        if current.data[staticListIndex] is None:
            return
        
        if current.size - 1 < STATIC_LIST_LENGTH // 2:
            if current.next is not None:
                # Sprawdzamy czy po usunieciu w bierzacej bedzie mniej niz polowa
                if current.size - 1 < STATIC_LIST_LENGTH // 2:
                    # Sprawdzamy czy po usunieciu z nastepnej bedzie mniejsza niz polowa
                    if current.next.size - 1 < STATIC_LIST_LENGTH // 2:
                        current.data[staticListIndex] = None

                        nextList = [el for el in current.next.data if el is not None]
                        currentList = [el for el in current.data if el is not None]

                        current.data = currentList + nextList
                        currentSize = len(current.data)
                        current.data += [None for _ in range(STATIC_LIST_LENGTH-currentSize)]
                        return

                    current.data[staticListIndex] = None
                    newElement = current.next.data[0]
                    current.next.data = current.next.data[1:] + [None]
                    addElementAtIndex(current.data, 0, newElement)
                    return

        current.data[staticListIndex] = None


    
    def printList(self) -> None:
        current = self.head
        while current is not None:
            print(f"{current.data} ", end="")
            current = current.next
        print()

    def toList(self):
        result = []
        current = self.head
        while current is not None:
            for el in current.data:
                result.append(el)
            current = current.next
        return result