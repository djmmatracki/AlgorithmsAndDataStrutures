from locale import currency
import random


class Node:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

# def randomLevel(p, maxLevel):
#     lvl = 1    
#     while random() < p and lvl <maxLevel: 
#         lvl = lvl + 1
#     return lvl


class SkipList:
    def __init__(self, maxStep):
        self.numLayers = random.randint(3, 15)
        self.head = [None for _ in range(self.numLayers)]
        self.maxStep = maxStep
    
    def printList(self):
        resultStr = ""

        for linked in self.head:
            current = linked

            while current is not None:
                resultStr += "(" + str(current.key) + "," + str(current.value) + ") "
                current = current.next
            
            resultStr += "\n"
        print(resultStr)
    

    def search(self, key):
        layer = 0

        while layer < self.numLayers:
            current = self.head[layer]
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
            layer += 1
        
        return None
    

    def delete(self, key):
        layer = 0

        while layer < self.numLayers:
            current = self.head[layer]

            if current is None:
                layer += 1
                continue

            if current.key == key:
                self.head[layer] = current.next
                layer += 1
                continue
                

            while current is not None:
                if current.key == key:
                    tail = current.next
                    beforeCurrent.next = tail
                    break

                beforeCurrent = current
                current = current.next
            layer += 1
        
        return None

    
    def insert(self, key, value):
        
        n = len(self.head)
        currentLayer = n - 1

        while currentLayer > 0:
            if self.head[currentLayer] is None:
                self.head[currentLayer] = Node(key, value)
                currentLayer -= 1
                continue

            if currentLayer != n - 1:
                if random.random() * (1 - (1 / (currentLayer))) < 0.5:
                    currentLayer -= 1
                    continue

            if self.head[currentLayer].key > key:
                head = self.head[currentLayer]
                newNode = Node(key, value)
                newNode.next = head
                self.head[currentLayer] = newNode
                currentLayer -= 1
                continue

            current = self.head[currentLayer]
            i = 0

            while current is not None and i < self.maxStep:

                if current.key > key:
                    newNode = Node(key, value)
                    beforeCurrent.next = newNode
                    newNode.next = current
                    break
                
                beforeCurrent = current
                current = current.next
                i += 1

            if current is None:
                beforeCurrent.next = Node(key, value)


            currentLayer -= 1


if __name__ == "__main__":

    skipList = SkipList(16)
    for i in range(1, 16):
        skipList.insert(i, chr(64+i))
    skipList.printList()