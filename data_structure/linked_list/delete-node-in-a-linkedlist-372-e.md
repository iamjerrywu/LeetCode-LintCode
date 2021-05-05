# Delete Node in a LinkedList 372 \(E\)

## Problem

Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.Example

**Example 1:**

```text
Input:
1->2->3->4->null
3
Output:
1->2->4->null
```

**Example 2:**

```text
Input:
1->3->5->null
3
Output:
1->5->null
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
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        if not node:
            return 
        node.val = node.next.val
        node.next = node.next.next
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

