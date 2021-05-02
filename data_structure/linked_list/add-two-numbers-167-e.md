# Add Two Numbers 167 \(E\)

## Problem

Description

You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in `reverse` order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.Example

**Example 1:**

```text
Input: 7->1->6->null, 5->9->2->null
Output: 2->1->9->null	
Explanation: 617 + 295 = 912, 912 to list:  2->1->9->null
```

**Example 2:**

```text
Input:  3->1->5->null, 5->9->2->null
Output: 8->0->8->null	
Explanation: 513 + 295 = 808, 808 to list: 8->0->8->null
```

## Solution

Traverse both linkedlist at the same time, and assign new node 

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
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        dummy = ListNode(None)
        tail = dummy

        carry = 0
        while l1 or l2 or carry:
            add_sum = 0
            if l1:
                add_sum+=l1.val
                l1 = l1.next
            if l2:
                add_sum+=l2.val
                l2 = l2.next
            add_sum+=carry
            digit, carry = add_sum%10, add_sum//10
            node = ListNode(digit)
            tail.next = node
            tail = node
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

