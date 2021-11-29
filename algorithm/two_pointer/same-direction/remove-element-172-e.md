# Remove Element 172 (E)

## Problem

Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.Example

```
Example 1:	Input: [], value = 0	Output: 0Example 2:	Input:  [0,4,4,0,0,2,4,4], value = 4	Output: 4		Explanation: 	the array after remove is [0,0,0,2]
```

## Solution - Two Pointers



{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        l, r = 0, 0
        while r < len(A):
            if A[r] != elem:
                A[l] = A[r]
                l+=1
            r+=1
        return l
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;

****

## Solution - Iteration (same idea as two pointers)



{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        l, r = 0, 0
        while r < len(A):
            if A[r] != elem:
                A[l] = A[r]
                l+=1
            r+=1
        return l
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
