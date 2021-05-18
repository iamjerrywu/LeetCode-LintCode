# Odd Even Linked List 1292 \(M\)

## Problem

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

The relative order inside both the even and odd groups should remain as it was in the input.  
The first node is considered odd, the second node even and so on ...Example

**Example1:**

```text
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```

**Example2:**

```text
Input: 2->1->null
Output: 2->1->null
```

## Solution 

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

from collections import deque
class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        if head is None:
            return head
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            odd.next = even_head
        return head
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

