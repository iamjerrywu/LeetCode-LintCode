# Implement Queue by Linked List II 493 \(E\)

## Problem

Description

Implement a Queue by linked list. Provide the following basic methods:

1. `push_front(item)`. Add a new item to the front of queue.
2. `push_back(item)`. Add a new item to the back of the queue.
3. `pop_front()`. Move the first item out of the queue, return it.
4. `pop_back()`. Move the last item out of the queue, return it.

Example

Example 1：

```text
Input：
push_front(1)
push_back(2)
pop_back() // return 2
pop_back() // return 1
push_back(3)
push_back(4)
pop_front() // return 3
pop_front() // return 4
```

Example 2：

```text
Input:
push_front(1)
pop_front()// return 1
```

## Solution - Doubly Linked-List

### Code

{% tabs %}
{% tab title="python" %}
```python
class DoubleListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Dequeue:
    
    def __init__(self):
        # do intialization if necessary
        self.head = None
        self.tail = None

    """
    @param: item: An integer
    @return: nothing
    """
    def push_front(self, item):
        # write your code here
        if not self.head:
            self.head = DoubleListNode(item)
            self.tail = self.head
        else:
            node = DoubleListNode(item)
            node.next = self.head
            self.head.prev = node
            self.head = node

    """
    @param: item: An integer
    @return: nothing
    """
    def push_back(self, item):
        # write your code here
        if not self.tail:
            self.tail = DoubleListNode(item)
            self.head = self.tail
        else:
            node = DoubleListNode(item)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    """
    @return: An integer
    """
    def pop_front(self):
        # write your code here
        if not self.head:
            return 
        val = self.head.val
        if self.head == self.tail:
            self.head = self.head.next
            self.tail = self.head
        else:
            self.head = self.head.next
            self.head.prev = None
        return val
        

    """
    @return: An integer
    """
    def pop_back(self):
        # write your code here
        if not self.tail:
            return 
        val = self.tail.val
        if self.head == self.tail:
            self.tail = self.tail.prev
            self.head = self.tail
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return val

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

