from typing import List


class Node:
    def __init__(self, text) -> None:
        self.text: str = text
        self.children: List[Node] = []
    
    def __str__(self) -> str:
        return self.text
    
    def __repr__(self) -> str:
        return self.text


def generateSuffixes(word):
    """Generate all suffixes for a word"""
    i = len(word) - 1
    result = []
    while i >= 0:
        result.append(word[i:])
        i -= 1
    return result

def generateSuffixTree(suffixes):
    tree = dict()
    # Jezeli niema suffixow zwracam None
    if len(suffixes) == 0:
        return
    
    # Jezeli jest jeden to zwracam go z kluczem na None czyli na koniec
    if len(suffixes) == 1:
        tree[suffixes[0]] = None
        return tree

    # Przeszukuje wszystkie suffixy i wstawiam do drzewa pierwsze litery jako korzenie
    for suffix in suffixes:
        if len(suffix) == 0:
            tree['\0'] = []
            continue

        if tree.get(suffix[0]) is None:
            tree[suffix[0]] = [suffix[1:]]
            continue

        tree[suffix[0]].append(suffix[1:])
    
    result = dict()

    for key, suffixes in tree.items():
        subTree = generateSuffixTree(suffixes)
        if subTree is None:
            result[key] = subTree
            continue

        # Kompresuje drzewo
        keys = list(subTree.keys())
        if len(keys) == 1:
            result[key + keys[0]] = subTree[keys[0]]
        else:
            result[key] = subTree

    return result


def findSuffixTree(tree, pattern):
    current = tree
    i = 1
    j = 0

    while i < len(pattern):
        print(current)
        res = current.get(pattern[j:i])

        if res is not None:
            current = res
            j += i
        else:
            i += 1



if __name__ == "__main__":
    suffixes = generateSuffixes("banana")
    tree = generateSuffixTree(suffixes)
    findSuffixTree(tree, "nan")