

class Node:
    def __init__(self, key, value, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        self.head = None

    def search(self, key):
        head = self.head

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


        return find_value(head, key)

