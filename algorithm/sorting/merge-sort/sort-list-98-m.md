# Sort List 98 \(M\)

## Problem

Sort a linked list in O\(nlogn\)O\(nlogn\) time using constant space complexity.Example

**Example 1:**

Input:

```text
list = 1->3->2->null
```

Output:

```text
1->2->3->null
```

Explanation:

Sort the linked list.

**Example 2:**

Input:

```text
list = 1->7->2->6->null
```

Output:

```text
1->2->6->7->null
```

Explanation:

Sort the linked list.Challenge

Solve it by merge sort & quick sort separately.

## Solution - Merge Sort

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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)  
    
    def find_mid(self, head):
        slow, fast = head, head
        # cannot write as "while fast and fast.next"
        # otherwise, when list length of two, i.e: [2,3]
        # the middle would always be 3, then infinity loop on the left side as [2, 3]
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow  
    
    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        else:
            tail.next = head2
        return dummy.next

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

