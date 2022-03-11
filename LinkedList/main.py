

class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def destroy(self) -> None:
        self.head = None

    def add(self, data) -> None:
        new = Node(data)
        new.next = self.head
        self.head = new

    def remove(self) -> None:
        self.head = self.head.next

    def is_empty(self) -> bool:
        return self.head is None
    
    def length(self) -> int:
        current = self.head
        lenght = 0
        while current is not None:
            current = current.next
            lenght += 1

        return lenght
    
    def addToEnd(self, data) -> None:
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        beforeCurrent = current

        while current is not None:
            beforeCurrent = current
            current = current.next

        beforeCurrent.next = Node(data)
    
    def removeFromEnd(self):
        current = self.head

        while current is not None:
            beforeCurrent = current
            current = current.next

        beforeCurrent.next = None

    
    def get(self):
        return self.head.data
    
    def printList(self) -> None:
        current = self.head
        while current is not None:
            print(f"{current.data} ", end="")
            current = current.next
    
    def take(self, n):
        if n < 0:
            return None

        i = 0
        newHead = Node(self.head.data)
        current = self.head
        currentNew = newHead

        while i < n - 1 and current is not None:
            current = current.next
            currentNew.next = Node(current.data)
            currentNew = currentNew.next
            i += 1

        newList = LinkedList()
        newList.head = newHead
        return newList

    def drop(self, n):
        if n < 0:
            return None

        i = 0
        current = self.head

        while i < n and current is not None:
            current = current.next
            i += 1
        
        if current is None:
            return LinkedList()
        
        newHead = Node(current.data)
        currentNew = newHead
        current = current.next

        while current is not None:
            currentNew.next = Node(current.data)
            currentNew = currentNew.next
            current = current.next

        newList = LinkedList()
        newList.head = newHead
        return newList

    def toList(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

