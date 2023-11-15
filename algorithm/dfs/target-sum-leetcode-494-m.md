# Target Sum (LeetCode 494) (M)

## Problem

You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

* For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

&#x20;

**Example 1:**

```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

**Example 2:**

```
Input: nums = [1], target = 1
Output: 1
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 20`
* `0 <= nums[i] <= 1000`
* `0 <= sum(nums[i]) <= 1000`
* `-1000 <= target <= 1000`



## Solution - DFS (TLE)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        return self.dfs(0, 0, nums, target)
    
    def dfs(self, index, sum_val, nums, target):
        cnt = 0
        if index == len(nums):
            if sum_val == target:
                return 1
            return 0
        
        cnt+=self.dfs(index + 1, sum_val + nums[index], nums, target)
        cnt+=self.dfs(index + 1, sum_val - nums[index], nums, target)
        return cnt
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



## Solution - DFS (Memoization)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(n * Total) Total = 2 * sum(nums)
        memo = {} # memo[(i, sum_val)] => starting from ith index with sum_val, how many times we reach the final target 
        return self.dfs(0, 0, nums, target, memo)
    
    def dfs(self, index, sum_val, nums, target, memo):
        if (index, sum_val) in memo:
            return memo[(index, sum_val)]
        
        cnt = 0
        if index == len(nums):
            if sum_val == target:
                return 1
            return 0
        
        memo[(index, sum_val)] = self.dfs(index + 1, sum_val + nums[index], nums, target, memo)
        memo[(index, sum_val)]+=self.dfs(index + 1, sum_val - nums[index], nums, target, memo)
        return memo[(index, sum_val)]
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

