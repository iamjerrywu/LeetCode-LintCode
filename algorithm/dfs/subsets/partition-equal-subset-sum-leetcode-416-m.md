# Partition Equal Subset Sum (LeetCode 416) (M)

## Problem

Given a **non-empty** array `nums` containing **only positive integers**, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

&#x20;

**Example 1:**

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 200`
* `1 <= nums[i] <= 100`

## Solution - DFS + Memoization

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_val = sum(nums)
        
        return self.dfs(0, 0, nums, sum_val, {})
    
    
    def dfs(self, index, sub_sum, nums, sum_val, memo):
        if sub_sum in memo:
            return memo[sub_sum]
        
        if sub_sum == sum_val/2:
            memo[sub_sum] = True
            return True
        
        for i in range(index, len(nums)):
            if self.dfs(i + 1, sub_sum + nums[i], nums, sum_val, memo):
                return True
        memo[sub_sum] = False
        return False
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

* **Time Complexity: O(m \* n)**
* **Space Complexity: O(m \* n)**
