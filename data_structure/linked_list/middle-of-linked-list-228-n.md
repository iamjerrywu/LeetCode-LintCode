# Middle of Linked List 228 \(N\)

## Problem

Description

Find the middle node of a linked list and return it.Example

**Example 1:**

```text
Input: 1->2->3
Output: 2
Explanation: return the middle node.
```

**Example 2:**

```text
Input: 1->2
Output: 1
Explanation: If the length of list is even return the center left one.
```

Challenge

If the linked list is a data stream, can you find the middle node without iterating the linked list again?

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
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if not head:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

