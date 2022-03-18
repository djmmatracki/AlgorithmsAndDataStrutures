
def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


class Queue:
    def __init__(self):
        self.end = 0
        self.start = 0
        self.queue = [None for _ in range(5)]
    
    def is_empty(self):
        return self.start == self.end
    
    def peek(self):
        return None if self.is_empty() else self.queue[self.start]
    
    def dequeue(self):
        if self.is_empty():
            return
        
        data = self.queue[self.start]
        self.queue[self.start] = None

        if len(self.queue) == self.start + 1:
            self.start = 0
        else:
            self.start += 1
        print(data)
        return data

    def enqueue(self, data) -> None:
        self.queue[self.end] = data

        if self.end + 1 == self.start or (self.end + 1 == len(self.queue) and self.start == 0):
            newSize = len(self.queue) * 2
            newTab = realloc(self.queue, newSize)
            i = newSize - self.start
            j = self.start

            while i < newSize:
                newTab[i] = self.queue[j]
                j += 1
                i += 1
            
            self.queue = newTab
            
        if self.end + 1 == len(self.queue):
            self.end = 0
            return

        self.end += 1
    
    def printQueue(self) -> None:
        result = "[ "
        start = self.start
        end = self.end

        while start != end:
            oldStart = start
            if start + 1 == len(self.queue):
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
