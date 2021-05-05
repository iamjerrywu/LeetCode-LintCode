# Swap Two Nodes in LinkedList 511 \(M\)

## Problem

Given a linked list and two values `v1` and `v2`. Swap the two nodes in the linked list with values `v1` and `v2`. It's guaranteed there is no duplicate values in the linked list. If v1 or v2 does not exist in the given linked list, do nothing.

You should swap the two nodes with values `v1` and `v2`. Do not directly swap the values of the two nodes.Example

**Example 1:**

```text
Input: 1->2->3->4->null, v1 = 2, v2 = 4
Output: 1->4->3->2->null
```

**Example 2:**

```text
Input: 1->null, v1 = 2, v2 = 1
Output: 1->null
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

class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        
        n1, n2 = None, None
        prev = dummy
        while head:
            if head.val == v1:
                n1 = head
                p1 = prev
            if head.val == v2:
                n2 = head
                p2 = prev
            prev = head
            head = head.next
        if not n1 or not n2:
            return dummy.next
        else:
            p1.next = n2
            tmp = n2.next
            if n1 == p2:
                n2.next = n1
            else:
                n2.next = n1.next
                p2.next = n1
            n1.next = tmp
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

