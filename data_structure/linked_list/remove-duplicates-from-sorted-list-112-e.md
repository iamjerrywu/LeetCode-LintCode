# Remove Duplicates from Sorted List 112 \(E\)

## Problem

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example

```text
Example 1:
	Input:  null
	Output: null


Example 2:
	Input:  1->1->2->null
	Output: 1->2->null
	
Example 3:
	Input:  1->1->2->3->3->null
	Output: 1->2->3->null
	
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
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
               head.next = head.next.next
            else:
                head = head.next
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

