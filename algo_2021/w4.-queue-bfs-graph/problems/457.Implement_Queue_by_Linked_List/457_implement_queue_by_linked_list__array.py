class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.MAXSIZE = 10000000
        self.queue = [0] * self.MAXSIZE
        self.head, self.tail = 0, 0

    def enqueue(self, item):
        # write your code here
        # if queue full
        if self.tail == self.MAXSIZE:
            return
        self.queue[self.tail] = item
        self.tail += 1
        

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        # if queue empty
        if self.head == self.tail:
            return -1
        item = self.queue[self.head]
        self.head += 1 
        return item