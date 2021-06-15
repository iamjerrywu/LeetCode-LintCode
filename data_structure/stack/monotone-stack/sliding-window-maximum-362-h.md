# Sliding Window Maximum 362 \(H\)

## Problem

Given an array of n integer with duplicate number, and a moving window\(size k\), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.Example

**Example 1:**

```text
Input:[1,2,7,7,8]3输出:[7,7,8]Explanation：At first the window is at the start of the array like this `[|1, 2, 7| ,7, 8]` , return the maximum `7`;then the window move one step forward.`[1, |2, 7 ,7|, 8]`, return the maximum `7`;then the window move one step forward again.`[1, 2, |7, 7, 8|]`, return the maximum `8`;
```

**Example 2:**

```text
Input:[1,2,3,1,2,3]5Output:[3,3]Explanation:At first, the state of the window is as follows: ` [,2,3,1,2,1 | , 3] `, a maximum of ` 3 `;And then the window to the right one. ` [1, | 2,3,1,2,3 |] `, a maximum of ` 3 `;
```

Challenge

o\(n\) time and O\(k\) memory

## Solution - Brute Force Enumeration

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            max_val = max(nums[i:i + k])
            res.append(max_val)
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* k\)**
* **Space Complexity: O\(n\)**

## Solution - Heap

### Code

{% tabs %}
{% tab title="python" %}
```python
from heapq import heappush, heappop

class Heap:
    def __init__(self):
        self.minheap = []
        self.deleted_set = set()
    #O(logk)
    def push(self, index, val):
        heappush(self.minheap, (val, index))
    
    #O(logk)
    def _lazy_delete(self):
        while self.minheap and self.minheap[0][1] in self.deleted_set:
            heappop(self.minheap)
    
    #O(logk)
    def top(self):
        self._lazy_delete()
        return self.minheap[0]
    #O(logk)
    def pop(self):
        self._lazy_delete()
        heappop(self.minheap)
    
    # O(1)
    def delete(self, index):
        self.deleted_set.add(index)
    
    #O(1)
    def is_empty(self):
        return not bool(self.minheap)

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        
        max_values = []
        maxheap = Heap()
        for i in range(len(nums)):
            maxheap.push(i, -nums[i])
            if (i < k - 1):
                continue
            max_values.append(-maxheap.top()[0])
            maxheap.delete(i - k + 1)
        return max_value
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogk\)**
  * Traverse nums
  * Push, Delete: O\(logk\), O\(1\)
* **Space Complexity: O\(k\)**

\*\*\*\*

## Solution - Monotonic Queue

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        queue = collections.deque()
        res = []
        for i in range(len(nums)):
            print(queue)
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if i >= k - 1:
                print(i, queue)
                res.append(nums[queue[0]])
            
            if i - k + 1 == queue[0]:
                queue.popleft()
        
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

