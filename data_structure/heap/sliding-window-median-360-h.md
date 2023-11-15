# Sliding Window Median 360 (H)

## Problem

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

* For examples, if `arr = [2,3,4]`, the median is `3`.
* For examples, if `arr = [1,2,3,4]`, the median is `(2 + 3) / 2 = 2.5`.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return _the median array for each window in the original array_. Answers within `10-5` of the actual value will be accepted.

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
```

**Example 2:**

```
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
```

**Constraints:**

* `1 <= k <= nums.length <= 105`
* `231 <= nums[i] <= 231 - 1`

## Solution - Brute Force (Sorting)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        res = []
        if not nums:
            return res
        for i in range(len(nums) - k + 1):
            window = sorted(nums[i : i + k])
            res.append(self.get_median(window))
        return res

    def get_median(self, window):
        n = len(window)
        if n%2 == 0:
            return window[n//2 - 1]
        else:
            return window[n//2]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O((n - k) \* klogk)**
* **Space Complexity:**



## Solution - Heap (with O(n) remove)

0 <= len(max-heap) - len(min-heap) <= 1

![](<../../.gitbook/assets/Screen Shot 2021-06-19 at 2.13.13 AM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        
        max_heap, min_heap = [], []
        res = []
        first = nums[0]

        for i in range(k):
            self.add(nums[i], max_heap, min_heap)     
        res.append(self.get_median(max_heap, min_heap))
        
        for i in range(k, len(nums)):
            self.remove(first, max_heap, min_heap)
            self.add(nums[i], max_heap, min_heap)
            res.append(self.get_median(max_heap, min_heap))
            first = nums[i - k + 1]
        return res
    
    def add(self, val, max_heap, min_heap):
        if not max_heap:
            heapq.heappush(max_heap, -val)
            return 
        if val > -max_heap[0]:
            heapq.heappush(min_heap, val)
        else:
            heapq.heappush(max_heap, -val)
        self.adjust_size(max_heap, min_heap)
    
    def adjust_size(self, max_heap, min_heap):
        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    def get_median(self, max_heap, min_heap):
        return -max_heap[0]
    
    def remove(self, val, max_heap, min_heap):
        if -val in max_heap:
            max_heap.remove(-val)
            heapq.heapify(max_heap)
        else:
            min_heap.remove(val)
            heapq.heapify(min_heap)  
        self.adjust_size(max_heap, min_heap)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O((n - k) \* k)**
* **Space Complexity: O(n)**



## Solution - Heap with O(1) remove

### Code

{% tabs %}
{% tab title="python" %}
```python
from heapq import heappush, heappop

class Heap:
    def __init__(self):
        self.minheap = []
        self.num_set = {}
        self.size = 0
    
    #O(logk)
    def push(self, value, index):
        heappush(self.minheap, (value, index))
        self.num_set[index] = value
        self.size+=1   
    
    #O(logk)
    def _lazy_delete(self):
        while self.minheap and self.minheap[0][1] not in self.num_set:
            heappop(self.minheap)
    
    #O(logk)
    def top(self):
        self._lazy_delete()
        return self.minheap[0]
    
    #O(logk)
    def pop(self):
        self._lazy_delete()
        self.num_set.pop(self.top()[1])
        self.size-=1
        return heappop(self.minheap)
    
    # O(1)
    def delete(self, index):
        if index in self.num_set:
            self.num_set.pop(index)
            self.size-=1 
    
    #O(1)
    def is_empty(self):
        return self.size == 0
    
    #O(1)
    def get_size(self):
        return self.size

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        
        max_heap, min_heap = Heap(), Heap()
        res = []
        first = 0

        for i in range(k):
            self.add(nums[i], i, max_heap, min_heap)
        res.append(self.get_median(max_heap, min_heap))
        
        for i in range(k, len(nums)):
            self.remove(first, max_heap, min_heap)
            self.add(nums[i], i, max_heap, min_heap)
            res.append(self.get_median(max_heap, min_heap))
            first = i - k + 1
        return res
    
    def add(self, val, index, max_heap, min_heap):
        if max_heap.is_empty():
            max_heap.push(-val, index)
            return 
        if val > -max_heap.top()[0]:
            min_heap.push(val, index)
        else:
            max_heap.push(-val, index)
        self.adjust_size(max_heap, min_heap)
    
    def adjust_size(self, max_heap, min_heap):
        if max_heap.get_size() < min_heap.get_size():
            val, index = min_heap.pop()           
            max_heap.push(-val, index)
        elif max_heap.get_size() > min_heap.get_size() + 1:
            val, index = max_heap.pop() 
            min_heap.push(-val, index)
    
    def get_median(self, max_heap, min_heap):
        return -max_heap.top()[0]
    
    def remove(self, index, max_heap, min_heap):
        max_heap.delete(index)
        min_heap.delete(index)
        self.adjust_size(max_heap, min_heap)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

