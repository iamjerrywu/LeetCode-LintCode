class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.size = 1000000
        self.queue = [0] * self.size
        self.head, self.tail = 0, 0
    def enqueue(self, item):
        # write your code here
        if (self.tail + 1) % self.size == self.head:
            return 
        self.queue[self.tail] = item
        # circular array
        self.tail = (self.tail + 1) % self.size

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.head == self.tail:
            return -1
        item = self.queue[self.head]
        # circular array
        self.head = (self.head + 1) % self.size
        return item
        
