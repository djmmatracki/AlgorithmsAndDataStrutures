

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


class AVLNode(Node):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    @property
    def left_height(self):
        return find_height(self.left)

    @property
    def right_height(self):
        return find_height(self.right)


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


def insert_node(head, key, value):
    if head is None:
        return AVLNode(key, value)
    
    if head.key == key:
        head.value = value
        return head

    if head.key > key:
        head.left = insert_node(head.left, key, value)
        return head
    
    if head.key < key:
        head.right = insert_node(head.right, key, value)
        return head


def resolve_left_imbalance(head):
    left_node = head.left

    # LL imbalance
    if left_node.left_height - left_node.right_height >= 0:
        left_right = left_node.right
        left_node.right = head
        head.left = left_right

        return left_node

    # LR imbalance
    new_head = left_node.right
    new_head_left = new_head.left
    new_head_right = new_head.right
    new_head.left = left_node
    new_head.right = head
    left_node.right = new_head_left
    head.left = new_head_right

    return new_head


def resolve_right_imbalance(head):
    right_node = head.right

    # RR imbalance
    if right_node.right_height - right_node.left_height >= 0:
        right_node_left = right_node.left
        right_node.left = head
        head.right = right_node_left
        return right_node

    # RL imbalance
    new_head = right_node.left
    new_head_left = new_head.left
    new_head_right = new_head.right
    new_head.left = head
    new_head.right = right_node

    right_node.left = new_head_right
    head.right = new_head_left

    return new_head


def find_imbalance(head):
    if head.right_height < 2 and head.left_height < 2:
        return head

    if head.left_height - head.right_height == 2:
        head = resolve_left_imbalance(head)

    if head.right_height - head.left_height == 2:
        head = resolve_right_imbalance(head)
    
    if head.left is not None:
        head.left = find_imbalance(head.left)
    
    if head.right is not None:
        head.right = find_imbalance(head.right)
    
    return head


class AVLTree(BinaryTree):
    def __init__(self) -> None:
        super().__init__()
    
    def insert(self, key, value):
        if self.head is None:
            self.head = AVLNode(key, value)
        insert_node(self.head, key, value)
        self.head = find_imbalance(self.head)

    def delete(self, key):
        super().delete(key)
        if self.head.left_height - self.head.right_height == 2:
            self.head = resolve_left_imbalance(self.head)

        if self.head.right_height - self.head.left_height == 2:
            self.head = resolve_right_imbalance(self.head)


if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(50, 'A')
    tree.insert(15, 'B')
    tree.insert(62, 'C')
    tree.insert(20, 'D')
    tree.insert(25, 'D')
    tree.insert(2, 'E')
    tree.insert(1, 'F')
    tree.insert(11, 'G')
    tree.insert(100, 'H')
    tree.insert(7, 'I')
    tree.insert(6, 'J')
    tree.insert(55, 'K')
    tree.insert(52, 'L')
    tree.insert(51, 'M')
    tree.insert(57, 'N')
    tree.insert(8, 'O')
    tree.insert(9, 'P')
    tree.insert(10, 'R')
    tree.insert(99, 'S')
    tree.insert(12, 'T')
    tree.print_tree()
    # Wyswietl klucz: wartosc
    tree.search(10)
    tree.delete(50)
    tree.delete(52)
    tree.delete(11)
    tree.delete(57)
    tree.delete(1)
    tree.delete(12)
    tree.insert(3, 'AA')
    tree.insert(4, 'BB')
    tree.delete(7)
    tree.delete(8)
    tree.print_tree()
    # Wyswietl klucz: wartosc
