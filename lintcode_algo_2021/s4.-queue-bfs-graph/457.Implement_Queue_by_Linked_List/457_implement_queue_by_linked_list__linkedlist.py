class Node:
    def __init__(self, _val):
        self.val = _val
        self.next = None
        

class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.head, self.tail = None, None

    def enqueue(self, item):
        # write your code here
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        # queue empty
        if not self.head:
            return -1000
        item = self.head.val
        self.head = self.head.next
        return item
