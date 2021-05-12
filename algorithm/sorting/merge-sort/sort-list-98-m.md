# Sort List 98 \(M\)

## Problem

Sort a linked list in O\(nlogn\)O\(nlogn\) time using constant space complexity.Example

**Example 1:**

Input:

```text
list = 1->3->2->null
```

Output:

```text
1->2->3->null
```

Explanation:

Sort the linked list.

**Example 2:**

Input:

```text
list = 1->7->2->6->null
```

Output:

```text
1->2->6->7->null
```

Explanation:

Sort the linked list.Challenge

Solve it by merge sort & quick sort separately.

## Solution - Merge Sort

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)  
    
    def find_mid(self, head):
        slow, fast = head, head
        # cannot write as "while fast and fast.next"
        # otherwise, when list length of two, i.e: [2,3]
        # the middle would always be 3, then infinity loop on the left side as [2, 3]
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow  
    
    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        else:
            tail.next = head2
        return dummy.next

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Quick Sort

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head

        mid = self.find_mid(head)

        left_dummy = ListNode(0)
        left_tail = left_dummy
        right_dummy = ListNode(0)
        right_tail = right_dummy
        mid_dummy = ListNode(0)
        mid_tail = mid_dummy
        
        # if value < mid, put behind left.dummy
        # if value == mid, put behind mid.dummy
        # if vlaue > mid, put behind right.dummy
        while head:
            if head.val < mid.val:
                left_tail.next = head
                left_tail = head
            elif head.val > mid.val:
                right_tail.next = head
                right_tail = head
            else:
                mid_tail.next = head
                mid_tail = head
            head = head.next
        
        left_tail.next = None
        right_tail.next = None
        mid_tail.next = None

        left = self.sortList(left_dummy.next)
        right = self.sortList(right_dummy.next)
        
        return self.concat(left, mid_dummy.next, right)

    def find_mid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def concat(self, left, mid, right):
        dummy = ListNode(0)
        tail = dummy
        
        tail.next = left
        tail = self.get_tail(tail)
        tail.next = mid
        tail = self.get_tail(tail)
        tail.next = right
        tail = self.get_tail(tail)
        return dummy.next
    
    def get_tail(self, head):
        if not head:
            return None
        # WARNING!
        # since want to get the tail node, cannot write as 'while not head'
        while head.next:
            head = head.next
        return head
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

