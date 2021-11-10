# Count Number of Maximum Bitwise-OR Subsets (LeetCode 2044) (M)

## Problem

&#x20;

Given an integer array `nums`, find the **maximum** possible **bitwise OR** of a subset of `nums` and return _the **number of different non-empty subsets** with the maximum bitwise OR_.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`. Two subsets are considered **different** if the indices of the elements chosen are different.

The bitwise OR of an array `a` is equal to `a[0] `**`OR`**`  a[1]  `**`OR`**`  ...  `**`OR`**` a[a.length - 1]` (**0-indexed**).

&#x20;

**Example 1:**

```
Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
```

**Example 2:**

```
Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
```

**Example 3:**

```
Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 16`
* `1 <= nums[i] <= 105`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def __init__(self):
        self.max_cnt = 0
        self.max_val = 0
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.dfs(0, [], nums)
        return self.max_cnt
    
    def dfs(self, index, tmp, nums):
        if len(tmp) > 0:
            val = tmp[0]
            for i in range(1, len(tmp)):   
                val|=tmp[i]
            if val > self.max_val:
                self.max_val = val
                self.max_cnt = 1
            elif val == self.max_val:
                self.max_cnt+=1
     
        for i in range(index, len(nums)):
            tmp.append(nums[i])
            self.dfs(i + 1, tmp, nums)
            tmp.pop()
                
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity:**
