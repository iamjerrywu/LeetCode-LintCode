# Add Two Numbers II (LeetCode 445) (M)

## Problem

You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg)

<pre><code>Input: l1 = [7,2,4,3], l2 = [5,6,4]
<strong>Output:
</strong> [7,8,0,7]</code></pre>

**Example 2:**

<pre><code>Input: l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:
</strong> [8,0,7]</code></pre>

**Example 3:**

<pre><code>Input: l1 = [0], l2 = [0]
<strong>Output:
</strong> [0]</code></pre>

&#x20;

**Constraints:**

* The number of nodes in each linked list is in the range `[1, 100]`.
* `0 <= Node.val <= 9`
* It is guaranteed that the list represents a number that does not have leading zeros.

\




## Solution - Reverse LinkedList

{% tabs %}
{% tab title="Python" %}
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        dummy = ListNode(0)
        head = dummy
        carry, digit, sum_val = 0, 0, 0
        while l1 or l2 or carry:
            if l1:
                sum_val+=l1.val
                l1 = l1.next
            if l2:
                sum_val+=l2.val
                l2 = l2.next
            sum_val+=carry
            digit = sum_val%10
            carry = sum_val//10
            head.next = ListNode(digit)
            head = head.next
            sum_val = 0
        node = self.reverse(dummy.next)
        return node
    
    def reverse(self, node):
        last = None
        while node:
            nxt = node.next
            node.next = last
            last = node
            node = nxt
        return last
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
