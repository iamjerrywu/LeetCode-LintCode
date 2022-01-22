# Kth Missing Positive Number (LeetCode1539) (E)

## Problem

Given an array `arr` of positive integers sorted in a **strictly increasing order**, and an integer `k`.

_Find the_ `kth` _positive integer that is missing from this array._

&#x20;

**Example 1:**

```
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
```

**Example 2:**

```
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
```

&#x20;

**Constraints:**

* `1 <= arr.length <= 1000`
* `1 <= arr[i] <= 1000`
* `1 <= k <= 1000`
* `arr[i] < arr[j]` for `1 <= i < j <= arr.length`



## Solution - Linear Search

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        ptr = 0
        while True:
            
            if k == 0:
                return i - 1
            
            if ptr < len(arr):
                if arr[ptr] == i:
                    ptr+=1
                else:
                    k-=1
            else:
                k-=1
            i+=1
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

## Solution - Binary Search

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if arr[mid] - mid - 1 < k:
                start = mid
            else:
                end = mid
                
        # arr[index] - index  - 1: means how many missing positive integer before index
        # to backtrack how many steps: (arr[index] - index - 1) - k + 1
        # so, it would be arr[index] - ((arr[index] - index - 1) - k + 1)
        # simplified as: index - k
        if arr[start] - start - 1 >= k:
            return start + k
        if arr[end] - end - 1 >= k:
            return end + k
        return end + 1 + k
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

* **Time Complexity: O(logn)**
* **Space Complexity:**

****

****
