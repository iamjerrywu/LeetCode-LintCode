# Insertion Sort List 173 \(E\)

## Problem

Sort a linked list using insertion sort.Example

```text
Example 1:
	Input: 0->null
	Output: 0->null


Example 2:
	Input:  1->3->2->0->null
	Output :0->1->2->3->null
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
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(0)
        while head:
            temp = dummy
            next = head.next
            print(temp.next)
            while temp.next and temp.next.val < head.val:
                temp = temp.next

            head.next = temp.next
            temp.next = head
            head = next
        
        return dummy.next
        

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

