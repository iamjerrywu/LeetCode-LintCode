# Insert Node in Sorted Linked List 219 \(E\)

## Problem



Insert a node in a sorted linked list.Example

**Example 1:**

```text
Input: head = 1->4->6->8->null, val = 5
Output: 1->4->5->6->8->null
```

**Example 2:**

```text
Input: head = 1->null, val = 2
Output: 1->2->null
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
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.val < val:
            cur = cur.next
        
        node = ListNode(val)
        node.next = cur.next
        cur.next = node
        
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

