# Rotate List 170 \(M\)

## Problem

Given a list, rotate the list to the right by `k` places, where _k_ is non-negative.Example

**Example 1:**

```text
Input:1->2->3->4->5  k = 2
Output:4->5->1->2->3
```

**Example 2:**

```text
Input:3->2->1  k = 1
Output:1->3->2
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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def getLength(self, head):
        length = 0
        while head:
            length+=1
            head = head.next
        return length
    
    def rotateRight(self, head, k):
        # write your code here
        if head is None: 
            return None
        dummy = ListNode(None, head)
        
        length = self.getLength(head)
        k %= length
        
        #ahead
        ahead = dummy
        for _ in range(k):
            ahead = ahead.next
        
        #behind
        behind = dummy
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        
        #rotate
        ahead.next = dummy.next
        dummy.next = behind.next
        behind.next = None
        
        return dummy.next
```
{% endtab %}

{% tab title="java" %}
```java
/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param head: the List
     * @param k: rotate to the right k places
     * @return: the list after rotation
     */
    public int getLength(ListNode head) {
        int length = 0;
        while(head != null) {
            head = head.next;
            length+=1;
        }
        return length;
    }
    
    public ListNode rotateRight(ListNode head, int k) {
        // write your code here
        if (head == null)
            return null;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        int length = getLength(head);
        k%= length;
        
        // ahead
        ListNode ahead = dummy;
        for ( int i = 0 ; i < k ; i ++ ) {
            ahead = ahead.next;
        }
        
        // behind
        ListNode behind = dummy;
        while(ahead.next != null) {
            ahead = ahead.next;
            behind = behind.next;
        }
        
        // rotate
        ahead.next = dummy.next;
        dummy.next = behind.next;
        behind.next = null;
        
        return dummy.next; 
        
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

