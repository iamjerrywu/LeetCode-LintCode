# Max Consecutive Ones III (LeetCode 1004) (M)

## Problem

&#x20;

Given a binary array `nums` and an integer `k`, return _the maximum number of consecutive_ `1`_'s in the array if you can flip at most_ `k` `0`'s.

&#x20;

**Example 1:**

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

**Example 2:**

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `nums[i]` is either `0` or `1`.
* `0 <= k <= nums.length`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_cnt = 0
        ans = 0
        
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt+=1
            
            while zero_cnt > k:
                if nums[j] == 0:
                    zero_cnt-=1
                j+=1
            ans = max(ans, i - j + 1)
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
