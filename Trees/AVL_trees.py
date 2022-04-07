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
    pass

def resolve_right_imbalance(head):
    pass


class AVLTree(BinaryTree):
    def __init__(self) -> None:
        super().__init__()
    
    def insert(self, key, value):
        if self.head is None:
            self.head = AVLNode(key, value)
        insert_node(key, value)

        result = find_inbalance(self.head)
        if result is not None:
            head, side = head

            if side == "left":
                resolve_left_imbalance(head)
                return
            resolve_right_imbalance(head)
