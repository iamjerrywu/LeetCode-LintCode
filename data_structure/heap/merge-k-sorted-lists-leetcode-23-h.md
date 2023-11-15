# Merge k Sorted Lists (LeetCode 23) (H)

## Problem





## Solution - Sort

{% tabs %}
{% tab title="Python" %}
```python
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        rec = []
        for lst in lists:
            while lst:
                rec.append(lst.val)
                lst = lst.next
        dummy = ListNode(-1)
        head = dummy
        rec.sort()
        
        for num in rec:
            head.next = ListNode(num)
            head = head.next
        return dummy.next
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

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(n)**



## Solution - Heap

{% tabs %}
{% tab title="Python" %}
```python
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, [lists[i].val, i])
        dummy = ListNode(-1)
        head = dummy
        while heap:
            # print(heap)
            val, index = heapq.heappop(heap)
            head.next = ListNode(val)
            head = head.next
            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(heap, [lists[index].val, index] )
        return dummy.next        
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

* **Time Complexity: O(nlogk)**
* **Space Complexity: O(k)**
