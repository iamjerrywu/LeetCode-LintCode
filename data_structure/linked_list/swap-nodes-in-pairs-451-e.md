# Swap Nodes in Pairs 451 \(E\)

## Problem

Given a linked list, swap every two adjacent nodes and return its head.Example

**Example 1:**

```text
Input: 1->2->3->4->null
Output: 2->1->4->3->null
```

**Example 2:**

```text
Input: 5->null
Output: 5->null
```

Challenge

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

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
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head 
        prev = head
        while head:
            if head.next:
                head = head.next
                if prev.val != head.val:
                    prev.val, head.val = head.val, prev.val
            head = head.next
            prev = head
        return dummy.next
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

