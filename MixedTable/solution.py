

class MixedTable:
    def __init__(self, size, c1=1, c2=0) -> None:
        self._table = [None for _ in range(size)]
        self.c1 = c1
        self.c2 = c2
    
    @property
    def size(self):
        return len(self._table)

    def __str__(self) -> str:
        stringRepr = "{\n"
        for el in self._table:
            if el is not None:
                key, val = el
                stringRepr += f"  {key}: {val},\n"
            else:
                stringRepr += "  None,\n"
        stringRepr += "}"
        return stringRepr

    def isIndexAvailable(self, index, key) -> bool:
        return self._table[index] is None or self._table[index][0] == key
    
    def isIndexTaken(self, index, key) -> bool:
        if self._table[index] is None:
            return False
        return self._table[index][0] == key

    
    def mixing(self, key, isAvailable):

        if not isinstance(key, (int, str)):
            raise ValueError("Klucz musi byc typem int lub str!")

        if isinstance(key, str):
            index = sum([ord(c) for c in key]) % self.size

        if isinstance(key, int):
            index = key % self.size

        if isAvailable(index, key):
            return index
        
        for i in range(self.size):
            new_index = (index + i*self.c1 + (i**2)*self.c2) % self.size
            if isAvailable(new_index, key):
                return new_index


    def insert(self, element):
        key, _ = element
        index = self.mixing(key, self.isIndexAvailable)
        if index is not None:
            self._table[index] = element
            return
        print("Brak miejsca")

    
    def remove(self, key):
        index = self.mixing(key, self.isIndexTaken)
        if index is not None:
            self._table[index] = None
            return
        raise KeyError("Key not found.")
    

    def get(self, __key):
        index = self.mixing(__key, self.isIndexTaken)
        if index is not None:
            return self._table[index][1]


def test_func1(size, c1, c2):
    table = MixedTable(size, c1, c2)

    for i in range(1, 16):
        if i == 6:
            table.insert((18, chr(64+i)))
        elif i == 7:
            table.insert((31, chr(64+i)))
        else:
            table.insert((i, chr(64+i)))
    print(table)
    print(table.get(5))
    print(table.get(14))
    table.insert((5, 'Z'))
    print(table.get(5))
    table.remove(5)
    print(table)
    print(table.get(31))
    table.insert(('test', 'W'))
    print(table)

def test_func2(size, c1, c2):
    table = MixedTable(size, c1, c2)

    for i in range(1, 16):
        table.insert((i*13, chr(64+i)))

    print(table)

test_func1(13, 1, 0)
test_func2(13, 1, 0)
test_func2(13, 0, 1)
test_func1(13, 0, 1)
