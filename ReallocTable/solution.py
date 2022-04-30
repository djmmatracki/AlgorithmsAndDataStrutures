
def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


class Queue:
    def __init__(self):
        self.end = 0
        self.start = 0
        self.queue = [None for _ in range(5)]
    
    @property
    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.start == self.end
    
    def peek(self):
        return None if self.is_empty() else self.queue[self.start]
    
    def dequeue(self):
        if self.is_empty():
            return
        
        data = self.queue[self.start]
        self.queue[self.start] = None

        if self.size == self.start + 1:
            self.start = 0
        else:
            self.start += 1

        return data

    def isListEmpty(self):
        for el in self.queue:
            if el is not None:
                return False
        return True

    def enqueue(self, data) -> None:
        if self.isListEmpty():
            self.queue[self.end] = data
            self.end += 1
            return

        if self.end == self.start or (self.end == self.size and self.start == 0):
            newSize = self.size * 2
            newTab = realloc(self.queue, newSize)
            i = newSize + self.start - len(self.queue)
            j = self.start

            while i < newSize:
                newTab[i] = self.queue[j]
                newTab[j] = None
                j += 1
                i += 1
            
            self.queue = newTab
            self.start = newSize - self.start
            
        if self.end == self.size:
            self.end = 1
        else:
            self.end += 1

        self.queue[self.end - 1] = data
    

    def printQueue(self) -> None:
        result = "[ "
        start = self.start
        end = self.end

        while start != end:
            oldStart = start
            if start + 1 == self.size:
                start = 0
            else:
                start += 1

            if self.queue[oldStart] is not None:
                result += f"{self.queue[oldStart]} "
            
        result += "]"
        print(result)


    def printList(self) -> None:
        print(self.queue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    print(queue.peek())
    queue.printQueue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.printList()

    while not queue.is_empty():
        queue.dequeue()

    queue.printQueue()
