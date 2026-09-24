# Odd Even Linked List (LeetCode 328) (M)

## Problem

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return _the reordered list_.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)

<pre><code><strong>Input: head = [1,2,3,4,5]
</strong><strong>Output: [1,3,5,2,4]
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)

<pre><code><strong>Input: head = [2,1,3,5,6,4,7]
</strong><strong>Output: [2,3,6,7,1,5,4]
</strong></code></pre>

&#x20;

**Constraints:**

* The number of nodes in the linked list is in the range `[0, 10`<sup>`4`</sup>`]`.
* `-10`<sup>`6`</sup>` ``<= Node.val <= 10`<sup>`6`</sup>



## Solution

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next ) return head;

        ListNode* odd = head;
        ListNode* even = head->next;

        // the start of the even chain never changes
        ListNode onst *evenHead = even;
        while(even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            
            even->next = odd->next;
            even = even->next;
        }
        // reconnect the end of odd list to the head of even list
        odd->next = evenHead;
        return head;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

