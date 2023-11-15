# Remove Linked List Elements 452 (E)

## Problem

Remove all elements from a linked list of integers that have value `val`.Example

**Example 1:**

```
Input: head = 1->2->3->3->4->5->3->null, val = 3
Output: 1->2->4->5->null
```

**Example 2:**

```
Input: head = 1->1->null, val = 1
Output: null
```

## Solution - Iteration

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

{% tab title="Java" %}
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while (head != null) {
            if (head.val == val) {
                prev.next = head.next;
            } else {
                prev = prev.next;
            }
            head = head.next;
        }
        return dummy.next;
    }   
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



## Solution - Recursion

### Code

{% tabs %}
{% tab title="python" %}

{% endtab %}

{% tab title="Java" %}
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        recursion(dummy, head, val);
        return dummy.next;
    }
    
    private void recursion(ListNode prev, ListNode cur, int val) {
        if (cur == null) return;
        if (cur.val == val) {
            prev.next = cur.next;
            recursion(prev, cur.next, val);
        } else {
            recursion(prev.next, cur.next, val);
        }
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
