# Remove Linked List Elements 452 \(E\)

## Problem

Remove all elements from a linked list of integers that have value `val`.Example

**Example 1:**

```text
Input: head = 1->2->3->3->4->5->3->null, val = 3
Output: 1->2->4->5->null
```

**Example 2:**

```text
Input: head = 1->1->null, val = 1
Output: null
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
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        dummy = ListNode(None, head)
        cur = dummy
        while cur.next != None: 
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
                
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

