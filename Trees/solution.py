

class Node:
    def __init__(self, key, value, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f"{self.key}: {self.value}"


def find_height(node):
    if node is None:
        return 0
    
    leftHeight = find_height(node.left)
    rightHeight = find_height(node.right)

    if leftHeight > rightHeight:
        return 1 + leftHeight
    return 1 + rightHeight


def insert_node(head, key, value):
    if head is None:
        return Node(key, value)
    
    if head.key == key:
        head.value = value
        return head

    if head.key > key:
        head.left = insert_node(head.left, key, value)
        return head
    
    if head.key < key:
        head.right = insert_node(head.right, key, value)
        return head


def find_value(head, key):
    if head is None:
        return None
    
    if head.key == key:
        return head.value

    if head.left is None and head.right is None:
        return

    if head.right is None:
        return find_value(head.left, key)
    
    if head.left is None:
        return find_value(head.right, key)
    
    if key < head.key:
        return find_value(head.left, key)

    return find_value(head.right, key)


def findMinValue(head):
    if head is None:
        return head
    
    if head.left is None:
        return head
    
    return findMinValue(head.left)


def delete_element(head, key):
    if head is None:
        return head
    
    if head.key > key:
        head.left = delete_element(head.left, key)
        return head
    
    if head.key < key:
        head.right = delete_element(head.right, key)
        return head

    if head.left is None:
        temp = head.right
        # head = None
        return temp
    
    if head.right is None:
        temp = head.left
        # head = None
        return temp
    
    temp = findMinValue(head.right)

    head.key = temp.key
    head.value = temp.value
    head.right = delete_element(head.right, temp.key)
    return head


class BinaryTree:
    def __init__(self) -> None:
        self.head = None

    def search(self, key):
        head = self.head
        return find_value(head, key)

    def insert(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
            return self.head
        return insert_node(self.head, key, value)

    def delete(self, key):
        self.head = delete_element(self.head, key)
        
    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)

            self._print_tree(node.left, lvl + 5)

    def height(self):
        return find_height(self.head)


# tree = BinaryTree()

# tree.insert(50, 'A')
# tree.insert(15, 'B')
# tree.insert(62, 'C')
# tree.insert(5, 'D')
# tree.insert(20, 'E')
# tree.insert(58, 'F')
# tree.insert(91, 'G')
# tree.insert(3, 'H')
# tree.insert(8, 'I')
# tree.insert(37, 'J')
# tree.insert(60, 'K')
# tree.insert(24, 'L')
# tree.print_tree()

# print(tree.search(24))
# print(tree.insert(20, "AA"))
# tree.insert(6, 'M')
# tree.delete(62)
# tree.insert(59, 'N')
# tree.insert(100, 'P')
# tree.delete(8)
# tree.delete(15)
# tree.insert(55, "R")
# tree.delete(50)
# tree.delete(5)
# tree.delete(24)
# print(tree.height())
# tree.print_tree()