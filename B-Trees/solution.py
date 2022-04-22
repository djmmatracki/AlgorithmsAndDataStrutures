

def insertKey(node, key):
    """Insert to leaf"""
    pass


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
                if node.keys[i] > key:
                    break
                i += 1

            if isLeaf(node):
                return insertKey(node, key)
            
            insertToNode(node.children[i], key)

        return insertToNode(self.root, key)