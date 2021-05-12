# Middle of the LinkedList 1609 \(E\)

## Problem

Given a non empty single linked list with head, please return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

The number of nodes in the given list will be between 1 and 100.Example

**Example 1:**

```text
Input: 1->2->3->4->5->null
Output: 3->4->5->null
```

**Example 2:**

```text
Input: 1->2->3->4->5->6->null
Output: 4->5->6->null
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
    @param head: the head node
    @return: the middle node
    """
    def middleNode(self, head):
        # write your code here.
        slow, fast = head, head
        # WARNING!
        # it ask the second of middle, shuold be fast/fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

