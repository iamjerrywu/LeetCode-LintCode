# Remove Duplicates from Unsorted List 217 \(E\)

## Problem

Write code to remove duplicates from an _unsorted_ linked list.Example

**Example 1:**

```text
Input: 1->2->1->3->3->5->6->3->null
Output: 1->2->3->5->6->null
```

**Example 2:**

```text
Input: 2->2->2->2->2->null
Output: 2->null
```

Challenge

\(hard\) How would you solve this problem if a temporary buffer is not allowed? In this case, you don't need to keep the order of nodes.

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
    @param head: The first node of linked list.
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here
        ref = set()
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        while head:
            if head.val not in ref:
                ref.add(head.val)
                prev = head
                head = head.next
            else: 
                if head.next:
                    prev.next = head.next
                    head = head.next
                else:
                    prev.next = None
                    head = None
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

