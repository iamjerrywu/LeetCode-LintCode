# Maximum Size Subarray Sum Equals k (LeetCode 325) (M)

## Problem



Given an integer array `nums` and an integer `k`, return _the maximum length of a subarray that sums to_ `k`. If there is not one, return `0` instead.

&#x20;

**Example 1:**

```
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
```

**Example 2:**

```
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 2 * 105`
* `-104 <= nums[i] <= 104`
* `-109 <= k <= 109`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sums = 0
        mapping = {0:-1}
        # mapping = {}
        ans = 0
        for i in range(len(nums)):
            prefix_sums+=nums[i]
            if prefix_sums not in mapping:
                mapping[prefix_sums] = i
            
            if prefix_sums - k in mapping:
                ans = max(ans, i - mapping[prefix_sums - k])
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
