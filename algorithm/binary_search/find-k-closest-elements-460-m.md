# Find K Closest Elements 460 (M)

## Problem

Description

Given `target`, a non-negative integer `k` and an integer array `A` sorted in ascending order, find the `k` closest numbers to `target` in `A`, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

1. The value `k` is a non-negative integer and will always be smaller than the length of the sorted array.
2. Length of the given array is positive and will not exceed 10^410​4​​
3. Absolute value of elements in the array will not exceed 10^410​4​​

Example

**Example 1:**

```
Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
```

**Example 2:**

```
Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
```

Challenge

O(logn + k) time

## Solution

![](<../../.gitbook/assets/Screen Shot 2021-04-24 at 12.13.52 AM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        # find the A[left] that's biggest < target
        # find the A[right] that's smallest >= target

        right = self.find_upper_closest(A, target)
        left = right - 1
        print(left, right)

        res = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                res.append(A[left])
                left-=1
            else:
                res.append(A[right])
                right+=1
        return res
    
    def find_upper_closest(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        # WARNING!
        # should find ">=" instead of "=="
        # because start would be closer to target
        if A[start] >= target:
            return start
        # WARNING!
        # should find ">=" instead of "=="
        if A[end] >= target:
            return end
        # if cannot find, return length
        return len(A)
    
    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        # if right out of bound, then left values are always valid
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target


```
{% endtab %}

{% tab title="Python (Better)" %}
```python
import collections
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find index 
        index = self.binary_search(0, len(arr) - 1, arr, x)

        k -=1
        res = collections.deque([arr[index]])
        l = index - 1
        r = index + 1
        # two pointers moving opposite direction
        while k > 0:
            if l >= 0 and r < len(arr):
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.appendleft(arr[l])
                    l-=1
                    k-=1
                else:
                    res.append(arr[r])
                    r+=1
                    k-=1
            elif l >= 0:
                res.appendleft(arr[l])
                l-=1
                k-=1
            else:
                res.append(arr[r])
                r+=1
                k-=1
        return res
    
    def binary_search(self, start, end, arr, x):
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if arr[mid] < x:
                start = mid
            else:
                end = mid
        print(start, end)
        if abs(arr[start] - x) <= abs(arr[end] - x):
            return start
        return end
            

```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
  * Binary Search: O(nlogn)
  * Two Pointer: O(k)
    * k <= n
* **Space Complexity: O(1)**

## Solution - Heap

{% tabs %}
{% tab title="Python" %}
```python
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for num in arr:
            heapq.heappush(heap, [-abs(num - x), -num])
            if len(heap) > k:
                heapq.heappop(heap)
                
        ans = [-val for dist, val in heap]
        ans.sort()
        return ans
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

