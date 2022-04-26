

def insertKey(node, key):
    """Insert to leaf"""
    
    # Sprawdzam czy wezel nie jest pelny
    if None not in node.keys:
        # Podzielic wezel, poniewaz node jest pelny
        # Zwraca srodkowy klucz z podzialu i wskazanie na nowo utworzony wezel
        return False

    # Wpisac w odpowiednie miejsce nowy klucz
    i = 0
    while i < len(node.keys):
        if node.keys[i] is None:
            node.keys[i] = key
            return

        if node.keys[i] > key:
            i -= 1
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
        self.keys = [None for _ in range(max_keys)]
        self.children = [None for _ in range(max_keys+1)]


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
                # Niema miejsca w leafie
                if result is None:
                    return
                # Zwracamy srodkowy klucz ktory musi byc dodany do parenta
                # oraz liste kluczy ktore musza byc przypisane do nowego noda
                return result

            result = insertToNode(node.children[i], key)

            if result is None:
                # Wezel nie zostal podzielony, konczymy
                return

            middleKey, newKeys = result
            
            if None not in node.keys:
                # Parent jest pelny
                pass
    
