

def insertKey(node, key):
    """Insert to leaf"""
    
    # Sprawdzam czy wezel nie jest pelny
    if None not in node.keys:
        # Podzielic wezel, poniewaz node jest pelny
        # Zwraca srodkowy klucz z podzialu i wskazanie na nowo utworzony wezel
        arr = node.keys + [key]
        arr.sort()
        
        n = len(node.keys)
        middle = arr[(n+1)//2]
        newKeys = [None for _ in range(n)]
        i = 0

        while len(arr)//2 + i +1 < len(arr):
            newKeys[i] = arr[len(arr)//2 + i + 1]
            i += 1
        
        k = 0

        while k < n:
            if k < (n+1) // 2:
                node.keys[k] = arr[k]
            else:
                node.keys[k] = None
            k += 1

        newNode = BNode(n)
        newNode.keys = newKeys

        k = (n+1)//2 + 1
        while k < (n + 1):
            newNode.children[k - (n+1)//2 - 1] = node.children[k]
            node.children[k] = None
            k += 1

        return middle, newNode

    # Wpisac w odpowiednie miejsce nowy klucz
    i = 0
    while i < len(node.keys):
        if node.keys[i] is None:
            node.keys[i] = key
            return

        if node.keys[i] > key:
            break
        i += 1
    
    temp = key

    while i < len(node.keys):
        temp1 = node.keys[i]
        node.keys[i] = temp
        temp = temp1
        i += 1



def isLeaf(node):
    for child in node.children:
        if child is not None:
            return False
    return True


class BNode:
    def __init__(self, max_keys) -> None:
        self.max_keys = max_keys
        self.keys = [None for _ in range(max_keys)]
        self.children = [None for _ in range(max_keys+1)]
    
    def __str__(self) -> str:
        return f"{self.keys} {self.children}"


# Przekuje aktualny wezel w przeszukaniu klucza wiekrzego od znalezionego
# Sprawdza czy jest lisciem
# Jezeli jest to dodaje klucz
# Jezeli nie to wola sie rekurencyjnie dla lewego potomka
# Po powrocie moze sie okazac ze potomek do ktorego przeszlismy zostal podzielony
# Tak wiec nalezy dodac do aktualnego wezla srodkowy klucz podzialy i wskazanie na nowo utworzony wezel
# Funkcja otrzymuje dodawany klucz oraz wskazanie na nowo-utworzony wezel ze swego poprzedniego wywolania
# Musi ona sprawdzic czy wezel nie jest pelny
#



class BTree:
    def __init__(self, max_keys) -> None:
        self.root = BNode(max_keys)
        self.max_keys = max_keys
    
    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(node.max_keys+1): 	                	
                self._print_tree(node.children[i], lvl+1)
                if i<node.max_keys:
                    print(lvl*'  ', node.keys[i])

    def insert(self, key):
        def insertToNode(node, key):
            i = 0

            # Szukamy miejsca w ktore trzeba wstawic node
            while i < self.max_keys:
                if node.keys[i] is None:
                    break

                if node.keys[i] > key:
                    break
                i += 1

            if isLeaf(node):
                result = insertKey(node, key)

                if result is None:
                    return
                # Zwracamy srodkowy klucz ktory musi byc dodany do parenta
                # oraz nowego noda
                if node == self.root:
                    # Tworzymy nowego roota z srodkowym elementem
                    # i wskazaniami na starego roota oraz nowy wezel
                    middleKey, newNode = result
                    newRoot = BNode(self.max_keys)
                    newRoot.keys[0] = middleKey
                    newRoot.children[0] = node
                    newRoot.children[1] = newNode
                    self.root = newRoot
                    return
                return result
            else:
                result = insertToNode(node.children[i], key)

                if result is None:
                    # Wezel nie zostal podzielony, konczymy
                    return

                middleKey, newNode = result
                # Dostajemy noda ktorego musimy dodac do aktualnego
                # oraz dostajemy middle key ktory musimy dodac

                # Probujemy dodac middle key
                res = insertKey(node, middleKey)
                # Jezeli sie nie uda to dostajemy noda oraz middle key

                # Jak dodamy to konczymy
                if res is None:
                    # Przesuwamy potomki aby wstawic nowy wezel
                    temp = newNode
                    while i < len(node.children) - 1:
                        temp1 = node.children[i+1]
                        node.children[i+1] = temp
                        temp = temp1
                        i += 1
                    return

                if node == self.root:
                    # Tworzymy nowego roota z srodkowym elementem
                    # i wskazaniami na starego roota oraz nowy wezel
                    newRootKey, newLeftNode = res
                    newRoot = BNode(self.max_keys)
                    newRoot.keys[0] = newRootKey
                    newRoot.children[0] = node
                    newRoot.children[1] = newLeftNode
                    self.root = newRoot
                    newLeftNode.children[self.max_keys//2] = newNode
                    return
                
                return result
            
        return insertToNode(self.root, key)
    

if __name__ == "__main__":

    tree = BTree(4)
    arr = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18, 15, 10, 19]

    for el in arr:
        tree.insert(el)
    tree.print_tree()

    tree1 = BTree(4)
    for i in range(20):
        tree1.insert(i)

    tree1.print_tree()

    for i in range(20, 200):
        tree1.insert(i)
    
    tree1.print_tree()

    tree2 = BTree(6)
    for i in range(200):
        tree2.insert(i)
    
    tree2.print_tree()