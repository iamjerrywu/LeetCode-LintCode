# Remove Duplicates from Sorted List II 113 \(M\)

## Problem

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.Example

_**Example 1**_

```text
Input : 1->2->3->3->4->4->5->null
Output : 1->2->5->null
```

_**Example 2**_

```text
Input : 1->1->1->2->3->null
Output : 2->3->null
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
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head 
        cur = head
        prev = dummy

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur_val = cur.val
                while cur and cur.val == cur_val:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
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

