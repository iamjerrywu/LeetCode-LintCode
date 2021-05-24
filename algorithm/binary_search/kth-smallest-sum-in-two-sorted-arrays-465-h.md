# Kth Smallest Sum In Two Sorted Arrays 465 \(H\)

## Problem

Given two integer arrays sorted in ascending order and an integer k. Define _sum = a + b_, where _a_ is an element from the first array and _b_ is an element from the second one. Find the _k_th smallest sum out of all possible sums.Example

**Example 1**

```text
Input:a = [1, 7, 11]b = [2, 4, 6]k = 3Output: 7Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 3th is 7.
```

**Example 2**

```text
Input:a = [1, 7, 11]b = [2, 4, 6]k = 4Output: 9Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 4th is 9.
```

**Example 3**

```text
Input:a = [1, 7, 11]b = [2, 4, 6]k = 8Output: 15Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 8th is 15.
```

Challenge

Do it in either of the following time complexity:

1. O\(k log min\(n, m, k\)\). where n is the size of A, and m is the size of B.
2. O\( \(m + n\) log maxValue\). where maxValue is the max number in A and B.

## Solution - Binary Search + Two Pointer

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        n = len(A)
        m = len(B)
        left = A[0] + B[0] - 1
        right = A[n - 1] + B[m - 1] + 1
        while left + 1 < right: # O(logmx)
            # count how many numbers that are smaller than or equal to k
            # if exceed, right = mid
            # if lower, left = mid
            mid = (left + right)//2
            if self.cal(mid, A, B) >= k:
                right = mid
            else:
                left = mid
        return right
    
    def cal(self, mid, A, B):
        n = len(A)
        m = len(B)
        cnt = 0
        start = 0
        end = m - 1
        while start <= n -1: #O(m + n)
            while end >= 0:
                if A[start] + B[end] > mid:
                    end -=1
                else:
                    break
            cnt += end + 1
            start +=1
        return cnt
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(\(m+n\)logmax\)**
  * m: len\(A\), n: len\(B\)
  * max: the max\(A, B\)
* **Space Complexity: O\(1\)**

\*\*\*\*

## Solution - Greedy + Heap

First put in the A\[0\] + B\[i\] \(i = 0 ~ len\(B\) - 1\) of element in to heap, then pop and put A\[i\] + B\[

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        heap = []
        for i in range(len(B)):
            heapq.heappush(heap, [A[0] + B[i], 0, i])
        while k > 1:
            k -= 1
            
            point = heapq.heappop(heap)
            value = point[0]
            a_id = point[1]
            b_id = point[2]

            if a_id == len(A) - 1:
                continue
            else:
                new_value = A[a_id + 1] + B[b_id]
                heapq.heappush(heap, [new_value, a_id + 1, b_id])
        return heapq.heappop(heap)[0]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(\(m+n\)logmax\)**
  * m: len\(A\), n: len\(B\)
  * max: the max\(A, B\)
* **Space Complexity: O\(1\)**

