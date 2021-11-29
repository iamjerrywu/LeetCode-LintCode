# Reverse Linked List II 36 (M)

## Problem

Description

Reverse a linked list from position `m` to `n`.

m and n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.Example

**Example 1:**

Input:

```
linked list = 1->2->3->4->5->NULL
m = 2
n = 4
```

Output:

```
1->4->3->2->5->NULL
```

Explanation:

Reverse the \[2,4] position of the linked list.

**Example 2:**

Input:

```
linked list = 1->2->3->4->null
m = 2
n = 3
```

Output:

```
1->3->2->4->NULL
```

Explanation:

Reverse the \[2,3] position of the linked list.Challenge

Reverse it in-place and in one-pass

## Solution - Brute Force

{% tabs %}
{% tab title="Python" %}
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
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        record = []
        cnt = 1
        cur = head
        while cur:
            if m <= cnt <= n:
                record.append(cur.val)
            cur = cur.next
            cnt+=1
        record.reverse()
        
        cnt = 1
        cur = head
        while cur:
            if m <= cnt <= n:
                cur.val = record[cnt - m]
            cnt+=1
            cur = cur.next
        return head
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**&#x20;
* **Space Complexity: O(n)**

## Solution

![](<../../.gitbook/assets/Screen Shot 2021-04-25 at 4.29.48 PM.png>)

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
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if m == n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        # before reverse part, just traverse
        for _ in range(m - 1):
            prev = prev.next
        cur = prev.next
        
        # from part that required reverse
        for _ in range(n - m):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        
        # the part after reverse, remained the same 
        
        return dummy.next
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
