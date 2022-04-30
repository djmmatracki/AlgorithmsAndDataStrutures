

class Element:
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority = priority
    
    def __gt__(self, other):
        return self.priority > other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __ge__(self, other):
        return self.priority >= other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    
    def __eq__(self, __o: object) -> bool:
        return self.priority == __o.priority
    
    def __str__(self) -> str:
        return f"{self.value} : {self.priority}"


class PriorityQueue:

    def __init__(self) -> None:
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def parent(self, index):
        """Returns index of parent node"""
        return (index - 1) // 2

    def left(self, index):
        """Returns index of left node"""
        return index * 2 + 1

    def right(self, index):
        """Returns index of right node"""
        return index * 2 + 2

    def peek(self):
        return self.queue[0]
    
    @property
    def size(self):
        return len(self.queue)

    def dequeue(self):
        if self.is_empty():
            return

        current = 0
        self.queue[current], self.queue[self.size - 1] = self.queue[self.size - 1], self.queue[current]
        value = self.queue.pop()

        if len(self.queue) == 0:
            return value

        while current < len(self.queue):
            leftIndex = self.left(current)
            rightIndex = self.right(current)

            if rightIndex >= len(self.queue):
                return value
            
            if self.queue[leftIndex] > self.queue[current]:
                if self.queue[leftIndex] >= self.queue[rightIndex]:
                    self.queue[current], self.queue[leftIndex] = self.queue[leftIndex], self.queue[current]
                    current = leftIndex
                    continue

            if self.queue[rightIndex] > self.queue[current]:
                if self.queue[rightIndex] >= self.queue[leftIndex]:
                    self.queue[current], self.queue[rightIndex] = self.queue[rightIndex], self.queue[current]
                    current = rightIndex
                    continue

            return value


    def enqueue(self, value, priority):
        newElement = Element(value, priority)

        if self.is_empty():
            self.queue.append(newElement)
            return

        self.queue.append(newElement)
        current = len(self.queue) - 1

        while current != 0:
            parentIndex = self.parent(current)
            if self.queue[parentIndex] < self.queue[current]:
                self.queue[parentIndex], self.queue[current] = self.queue[current], self.queue[parentIndex]
            current = parentIndex

    def print_tab(self):
        print ('{', end=' ')
        if self.size > 0:
            for i in range(self.size-1):
                print(self.queue[i], end = ', ')
            if self.queue[self.size-1]: print(self.queue[self.size-1] , end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx < len(self.queue):
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.queue[idx] if self.queue[idx] else None)            
            self.print_tree(self.left(idx), lvl+1)
    

if __name__ == "__main__":
    queue = PriorityQueue()
    keys = [4, 7, 6, 7, 5, 2, 2, 1]
    values = "ALGORYTM"

    for key, value in zip(keys, values):
        queue.enqueue(value, key)
    queue.print_tree(0, 0)
    queue.print_tab()
    print(queue.dequeue())
    print(queue.peek())
    queue.print_tab()

    while not queue.is_empty():
        print(queue.dequeue())
    queue.print_tab()