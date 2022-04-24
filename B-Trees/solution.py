

def insertKey(node, key):
    """Insert to leaf"""
    if None not in node.keys:
        return False

    i = 0
    while i < len(node.keys):
        if node.keys[i] is None:
            node.keys[i] = key
            return True

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

    return True


def isLeaf(node):
    for child in node.children:
        if child is not None:
            return False
    return True


class BNode:
    def __init__(self, max_keys) -> None:
        self.keys = [None for _ in range(max_keys)]
        self.children = [None for _ in range(max_keys+1)]


class BTree:
    def __init__(self, max_keys) -> None:
        self.root = BNode(max_keys)
        self.max_keys = max_keys

    def insert(self, key):
        def insertToNode(node, key):
            i = 0

            while i < self.max_keys:
                if node.keys[i] is None:
                    break

                if node.keys[i] > key:
                    break
                i += 1

            if isLeaf(node):
                # Dodajemy do wezla klucz
                # Jezeli wezel jest pelny to zwracamy False
                # Jezeli poprawnie wstawilismy to True
                added = insertKey(node, key)
                if added:
                    # Zwracamy ze nie nastapilo podzialu
                    return False

                # Musi natapic podzial
                return True
            
            return insertToNode(node.children[i], key)

        return insertToNode(self.root, key)