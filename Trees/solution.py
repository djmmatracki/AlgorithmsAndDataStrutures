
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


    def insert(self, key, value):
        
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
        
        if self.head is None:
            self.head = Node(key, value)
            return self.head

        return insert_node(self.head, key, value)


    def delete(self, key):

        def delete_element(head, key):
            if head is None:
                return None
            
            if head.key == key:
                return None

            if head.key > key:
                head.left = delete_element(head.left, key)
                return head
            
            if head.key < key:
                head.right = delete_element(head.right, key)
                return head
        
        return delete_element(self.head, key)
        


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
        def find_height(node):
            if node is None:
                return 0
            
            leftHeight = find_height(node.left)
            rightHeight = find_height(node.right)

            if leftHeight > rightHeight:
                return 1 + leftHeight
            return 1 + rightHeight

        return find_height(self.head)


tree = BinaryTree()

tree.insert(5, 2)
tree.insert(3, 3)
tree.insert(6, 4)
tree.insert(1, 5)
tree.insert(4, 6)
tree.insert(7, 3)
# tree.print_tree()
tree.print_tree()
# print(tree.height())