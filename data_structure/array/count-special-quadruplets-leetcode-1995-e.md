# Count Special Quadruplets \(LeetCode 1995\) \(E\)

## Problem

Given a **0-indexed** integer array `nums`, return _the number of **distinct** quadruplets_ `(a, b, c, d)` _such that:_

* `nums[a] + nums[b] + nums[c] == nums[d]`, and
* `a < b < c < d`

**Example 1:**

```text
Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
```

**Example 2:**

```text
Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].
```

**Example 3:**

```text
Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
```

**Constraints:**

* `4 <= nums.length <= 50`
* `1 <= nums[i] <= 100`

## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = self.dfs(0, 0, 0, nums)
        return ans
    def dfs(self,idx, sum_val, cnt, nums):
        ans = 0
        if cnt > 3:
            return 0
        for i in range(idx, len(nums)):
            if cnt == 3:
                if sum_val == nums[i]:
                    ans+=1 
            sum_val+=nums[i]
            if i + 1 < len(nums):
                ans+=self.dfs(i + 1, sum_val, cnt+1, nums)
            sum_val-=nums[i]
        return ans
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** 
* **Space Complexity:** 

\*\*\*\*

## Solution - For Loop 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            print(i, j, k, l)
                            ans+=1
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** 
* **Space Complexity:** 

