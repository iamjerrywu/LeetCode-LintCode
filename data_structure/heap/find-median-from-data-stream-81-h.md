# Find Median from Data Stream 81 (H)

## Problem

You are given a data stream in this problem, and you need to implement two functions as following:

* function `add(val)` : receive a num from the data stream.
* function `getMedian()` : return the `median` of the all numbers which you have received from the data stream.

**The `median` is not equal to `median` in math.**\
The `median` is the number that in the middle of a sorted array, if there are `n` numbers in a sorted array `A`, the median is `A[(n - 1) / 2]` .\
For example, if `A=[1,2,3]`, the median is `A[(3-1)/2] = A[1] = 2`, if `A=[1,19]`, median is `A[(2-1)/2] = A[0] = 1`.

There are 10^4104 numbers in the data stream at most.Example

**Example 1:**

Input:

```
add(1)getMedian()add(2)getMedian()add(3)getMedian()add(4)getMedian()add(5)getMedian()
```

Output:

```
11223
```

Explanation:

The median of \[1] and \[1,2] is 1,\
The median of \[1,2,3] and \[1,2,3,4] is 2,\
The median of \[1,2,3,4,5] is 3.\
**Example 2:**

Input:

```
add(4)getMedian()add(5)getMedian()add(1)getMedian()add(3)getMedian()add(2)getMedian()add(6)getMedian()add(0)getMedian()
```

Output:

```
4443333
```

Explanation:

The median of \[4], \[4,5], \[4,5,1] is 4.\
The median of \[4,5,1,3], \[4,5,1,3,2], \[4,5,1,3,2,6] and \[4,5,1,3,2,6,0] is 3.Challenge

Implement an algorithm with time complexity of O(n\*logn)O(n∗logn)

## Solution - Brute Force (Sorting)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def __init__(self):
        # do initialize if it is necessary
        self.nums = []


    """
    @param val: An integer
    @return: nothing
    """
    def add(self, val):
        # write your code here
        self.nums.append(val)


    """
    @return: return the median of the data stream
    """
    def getMedian(self):
        # write your code here
        if not self.nums:
            return 0
        
        n = len(self.nums)
        return sorted(self.nums)[(n - 1)//2]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * add(): O(1)
  * GetMedian(): O(nlogn)
* **Space Complexity:**

## Solution - Heap

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
class Solution:
    def __init__(self):
        # do initialize if it is necessary
        # self.nums = []
        self.min_heap = []
        self.max_heap = [] # median always put in here, 0 <= len(max_heap) - len(min_heap) <= 1

    """
    @param val: An integer
    @return: nothing
    """
    def add(self, val):
        # write your code here
        if not self.max_heap:
            heapq.heappush(self.max_heap, -val)
            return
        mid = -self.max_heap[0]
        if val <= mid:
            heapq.heappush(self.max_heap, -val)
        else:
            heapq.heappush(self.min_heap, val)
        
        # 0 <= len(max_heap) - len(min_heap) <= 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    """
    @return: return the median of the data stream
    """
    def getMedian(self):
        # write your code here
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0])/2
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * add(): logn
  * getMedian(): O(1)
* **Space Complexity:**
  * O(n)
