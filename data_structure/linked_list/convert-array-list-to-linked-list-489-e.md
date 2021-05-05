# Convert Array List to Linked List 489 \(E\)

## Problem

Description

Convert an array list to a linked list.Example

Example 1:

```text
Input: [1,2,3,4], 
Output: 1->2->3->4->null.
```

Example 2:

```text
Input: [1,2], 
Output: 1->2->null.
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
    @param: nums: an integer array
    @return: the first node of linked list
    """
    def toLinkedList(self, nums):
        # write your code here
        if not nums:
            return None
        
        dummy = ListNode(0)
        cur = ListNode(nums[0])
        dummy.next = cur
        for i in range(1, len(nums)): 
            cur.next = ListNode(nums[i])
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

