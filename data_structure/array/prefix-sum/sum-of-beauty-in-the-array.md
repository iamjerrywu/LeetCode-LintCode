# Sum of Beauty in the Array (LeetCode 2012) (M)

## Problem

You are given a **0-indexed** integer array `nums`. For each index `i` (`1 <= i <= nums.length - 2`) the **beauty** of `nums[i]` equals:

* `2`, if `nums[j] < nums[i] < nums[k]`, for **all** `0 <= j < i` and for **all** `i < k <= nums.length - 1`.
* `1`, if `nums[i - 1] < nums[i] < nums[i + 1]`, and the previous condition is not satisfied.
* `0`, if none of the previous conditions holds.

Return _the **sum of beauty** of all_ `nums[i]` _where_ `1 <= i <= nums.length - 2`.

**Example 1:**

```
Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
```

**Example 2:**

```
Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
```

**Example 3:**

```
Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.
```

**Constraints:**

* `3 <= nums.length <= 105`
* `1 <= nums[i] <= 105`

## Solution

Construct the maxPrefix from left, and the minPrefix from right, so when checking fist condition we don't need to traverse all the arrays again.

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        max_from_left = []
        min_from_right = collections.deque()
        
        max_val = 0
        for i in range(len(nums)):
            max_val = max(max_val, nums[i])
            max_from_left.append(max_val)
        min_val = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            min_val = min(min_val, nums[i])
            min_from_right.appendleft(min_val)
        
        ans = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > max_from_left[i - 1] and nums[i] < min_from_right[i + 1]:
                ans+=2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans+=1
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
