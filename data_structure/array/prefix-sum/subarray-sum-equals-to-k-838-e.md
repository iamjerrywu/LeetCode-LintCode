# Subarray Sum Equals to k 838 \(E\)

## Problem

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.Example

**Example1**

```text
Input: nums = [1,1,1] and k = 2
Output: 2
Explanation:
subarray [0,1] and [1,2]
```

**Example2**

```text
Input: nums = [2,1,-1,1,2] and k = 3
Output: 4
Explanation:
subarray [0,1], [1,4], [0,3] and [3,4]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        if not nums:
            return 0

        prefix_sum = 0
        prefix_sum_to_times = {0:1}
        
        cnt = 0
        for num in nums:
            prefix_sum+=num
            if prefix_sum - k in prefix_sum_to_times:
               cnt+=prefix_sum_to_times[prefix_sum - k] 
            prefix_sum_to_times[prefix_sum] = prefix_sum_to_times.get(prefix_sum, 0) + 1

        return cnt            

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        if not nums:
            return 0

        prefix_sum = 0
        prefix_sum_to_times = {0:1}
        
        cnt = 0
        for num in nums:
            prefix_sum+=num
            if prefix_sum - k in prefix_sum_to_times:
               cnt+=prefix_sum_to_times[prefix_sum - k] 
            prefix_sum_to_times[prefix_sum] = prefix_sum_to_times.get(prefix_sum, 0) + 1

        return cnt            

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

