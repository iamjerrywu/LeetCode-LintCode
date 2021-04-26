# Top k Largest Numbers 544 \(M\)

## Problem

Given an integer array, find the top _k_ largest numbers in it.Example

**Example1**

```text
Input: [3, 10, 1000, -99, 4, 100] and k = 3
Output: [1000, 100, 10]
```

**Example2**

```text
Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
Output: [8, 7, 6, 5, 4]
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return sorted(min_heap, reverse = True)
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

