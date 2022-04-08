from solution import BinaryTree, Node, find_height


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


def find_inbalance(head):
    if head is None:
        return None

    if head.left_height == 0 and head.right_height == 2:
        return head, "right"

    if head.right_height == 0 and head.left_height == 2:
        return head, "left"

    imbalance = head.right_height - head.left_height

    if imbalance > 1:
        return find_inbalance(head.right)
    
    if imbalance < -1:
        return find_inbalance(head.left)


def resolve_left_imbalance(head):
    left_node = head.left
    if left_node.left is None:
        head.right = AVLNode(key=head.key, value=head.value)
        head.key, head.value = left_node.right.key, left_node.right.value
        left_node.right = None
        return
    
    if left_node.right is None:
        head.right = AVLNode(key=head.key, value=head.value)
        head.key, head.value = left_node.key, left_node.value
        left_node.key, left_node.value = left_node.left.key, left_node.left.value
        left_node.left = None
        return


def resolve_right_imbalance(head):
    right_node = head.right

    if right_node.right is None:
        head.left = AVLNode(key=head.key, value=head.value)
        head.key, head.value = right_node.left.key, right_node.left.value
        right_node.left = None
        return

    if right_node.left is None:
        head.left = AVLNode(key=head.key, value=head.value)
        head.key, head.value = right_node.key, right_node.value
        right_node.key, right_node.value = right_node.right.key, right_node.right.value
        right_node.right = None
        return


class AVLTree(BinaryTree):
    def __init__(self) -> None:
        super().__init__()
    
    def insert(self, key, value):
        if self.head is None:
            self.head = AVLNode(key, value)
        insert_node(self.head, key, value)

        result = find_inbalance(self.head)
        if result is not None:
            head, side = result

            if side == "left":
                resolve_left_imbalance(head)
                return
            resolve_right_imbalance(head)

    def delete(self, key):
        super().delete(key)

        result = find_inbalance(self.head)
        if result is not None:
            head, side = head

            if side == "left":
                resolve_left_imbalance(head)
                return
            resolve_right_imbalance(head)


if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(50, 'A')
    tree.insert(15, 'B')
    tree.insert(62, 'C')
    tree.insert(5, 'D')
    tree.insert(2, 'E')
    tree.insert(1, 'F')
    # tree.insert(11, 'G')
    # tree.insert(100, 'H')
    # tree.insert(7, 'I')
    # tree.insert(6, 'J')
    # tree.insert(55, 'K')
    # tree.insert(52, 'L')
    # tree.insert(51, 'M')
    # tree.insert(57, 'N')
    # tree.insert(8, 'O')
    # tree.insert(9, 'P')
    # tree.insert(10, 'R')
    # tree.insert(99, 'S')
    # tree.insert(12, 'T')
    tree.print_tree()
    print(tree.head.left_height)
    print(tree.head.right_height)