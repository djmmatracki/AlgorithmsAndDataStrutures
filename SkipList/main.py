import random
from typing import Any, List, Optional


class Node:
    def __init__(self, layers, key: Any=None, value: Any=None) -> None:
        self.next: List[Optional[Node]] = [None for _ in range(layers)]
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"(key: {self.key}, value: {self.value})"


class SkipList:
    def __init__(self, layers: int) -> None:
        self.head: Node = Node(layers)
        self.numLayers = layers
    

    def search(self, key):
        n = self.numLayers
        layer = 0
        current = self.head.next[layer]

        while current is None and layer < n:
            current = self.head.next[layer]
            layer += 1
        
        if current is None:
            return

        beforeCurrent = self.head
        layer -= 1

        while layer < n:
            current = beforeCurrent.next[layer]

            while current is not None:
                if current.key == key:
                    return current

                if current.key > key:
                    layer += 1
                    break
                
                beforeCurrent = current
                current = current.next[layer]

            if current is None:
                layer += 1


    def delete(self, key):
        n = self.numLayers
        layer = 0

        while layer < n:
            current = self.head.next[layer]

            if current.key == key:
                self.head.next[layer] = current.next[layer]
                layer += 1
                continue

            while current is not None:
                if current.key == key:
                    beforeCurrent.next[layer] = current.next[layer]
                    break
                
                beforeCurrent = current
                current = current.next[layer]

            layer += 1


    def insert(self, key, value):

         # If this key is already in the list then stop
        node = self.search(key)
        if node is not None:
            node.value = value
            return

        # Warstwy w ktorych pojawi sie nowa wartosc
        inputLayers = {i for i in range(self.numLayers) if random.random() < (i+1) / self.numLayers}

        newNode = Node(self.numLayers, key, value)

        for layer in inputLayers:
            current = self.head.next[layer]

            if current is None:
                self.head.next[layer] = newNode
                continue

            if current.key > key:
                newNode.next[layer] = current
                self.head.next[layer] = newNode
                continue

            while current.key < key:
                beforeCurrent = current
                current = current.next[layer]

                if current is None:
                    beforeCurrent.next[layer] = newNode
                    break

            if current is not None:
                newNode.next[layer] = current
                beforeCurrent.next[layer] = newNode
        
    def printList(self):
        layer = 0
        while layer < self.numLayers:
            current = self.head.next[layer]
            while current is not None:
                print(f"{current.key}", end=" ")
                current = current.next[layer]
            print()
            layer += 1
        print()

            
if __name__ == "__main__":

    skipList = SkipList(5)

    for i in range(1, 16):
        skipList.insert(i, chr(64+i))
    skipList.printList()
    print(skipList.search(2))
    skipList.insert(2, 'Z')
    print(skipList.search(2))
    skipList.delete(5)
    skipList.delete(6)
    skipList.delete(7)
    skipList.printList()
    skipList.insert(6, 'W')
    skipList.printList()