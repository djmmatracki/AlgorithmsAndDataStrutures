from LinkedList.main import Node, LinkedList

# Operacje bazowe

def nil():
    """Return empty list"""
    return LinkedList()

def cons(val, head):
    """Add to begining"""
    new = Node(val)
    new.next = head
    head = new

def first(head):
    """Return first"""
    return head.data

def rest(head):
    """Return from second"""
    return head.next

###

def create():
    return nil()

def length(head):
    if head is None:
        return 0

    if head.next is None:
        return 1
        
    return 1 + length(head.next)
    

def is_empty(head):
    return head is None

def destroy(head):
    head = None
    return head


def addToEnd(head, val):
    if head is None:
        cons(val, head)
        return
    
    if head.next is None:
        head.next = Node(val)
        return
    addToEnd(head.next, val)


def removeFromEnd(head):
    if head is None:
        return
    
    if head.next is None:
        head = None
        return
    
    if head.next.next is None:
        head.next = None
        return
    
    removeFromEnd(head.next)

def take(head, n):
    if head is None or n < 1:
        return
    
    if n == 1:
        linked = LinkedList()
        linked.head = Node(head.data)
        return linked
    
    linked = LinkedList()
    newHead = Node(head.data)
    newHead.next = take(head.next, n-1).head

    linked.head = newHead
    return linked


def drop(head, n):
    
    if head is None:
        return
    
    if head.next is None and n < 1:
        newList = LinkedList()
        newList.head = Node(head.data)
        return newList
        
    if n > 0:
        return drop(head.next, n-1)
    
    newList = LinkedList()
    newList.head = Node(head.data)
    newList.head.next = drop(head.next, n).head

    return newList
