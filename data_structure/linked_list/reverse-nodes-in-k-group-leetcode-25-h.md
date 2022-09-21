# Reverse Nodes in k-Group (LeetCode 25) (H)

## Problem

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return _the modified list_.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse\_ex1.jpg)

<pre><code>Input: head = [1,2,3,4,5], k = 2
<strong>Output:
</strong> [2,1,4,3,5]</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse\_ex2.jpg)

<pre><code>Input: head = [1,2,3,4,5], k = 3
<strong>Output:
</strong> [3,2,1,4,5]</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the list is `n`.
* `1 <= k <= n <= 5000`
* `0 <= Node.val <= 1000`



## Solution&#x20;

Traverse the linked list, strategy will be:

1. Check if starting from cur there are at least k node afterward
   1. if yes, reverse all of them, and find the new_head, new\_tail_
   2. return cur as head

{% tabs %}
{% tab title="Python" %}
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        cur = head
        new_head = None
        prev_tail = None
        while cur:
            
            if self.check(cur, k):                
                new_cur, tmp_head, tmp_tail = self.reverse(cur, k)
                if not new_head:
                    new_head = tmp_head
                if prev_tail:
                    prev_tail.next = tmp_head
                prev_tail = tmp_tail
                cur = new_cur
            else:
                prev_tail.next = cur
                break
        return new_head
    
    def check(self, cur, k):
        while k:
            if not cur:
                return False
            cur = cur.next
            k-=1
        return True
    
    def reverse(self, cur, k):
        tmp_tail = cur
        
        node = None
        while k:
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
            k-=1
        return cur, node, tmp_tail
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
