# Number of Good Pairs \(LeetCode 1512\) \(E\)

## Problem

Given an array of integers `nums`, return _the number of **good pairs**_.

A pair `(i, j)` is called _good_ if `nums[i] == nums[j]` and `i` &lt; `j`.

**Example 1:**

```text
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
```

**Example 2:**

```text
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
```

**Example 3:**

```text
Input: nums = [1,2,3]
Output: 0
```

**Constraints:**

* `1 <= nums.length <= 100`
* `1 <= nums[i] <= 100`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # Brute Force
        # cnt = 0
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             cnt+=1
        # return cnt
        
        
        
        # if length of nums reach 10^5, then should use solution like here
        count = collections.Counter(nums)
        
        ans = 0
        for k, v in count.items():
            ans+= ((v - 1) + 1) * (v - 1) // 2
        return ans
        
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:**

