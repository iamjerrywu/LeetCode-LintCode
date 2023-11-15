# Jump Game II (LeetCode 45) (M)

## Problem

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

&#x20;

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [2,3,0,1,4]
Output: 2
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `0 <= nums[i] <= 1000`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        # traverse all the start point
        for i in range(n):
            # the steps you can move from ith position
            for j in range(nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        '''
        for i in range(n):
            for j in range(i, i + nums[i] + 1):
                if j < n and dp[i] != float('inf'):
                    dp[j] = min(dp[j], dp[i] + 1) 
        '''            
        return dp[-1]
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n)**

## Solution - Greedy

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0
        steps = 0
        cur = 0
        
        for i in range(n - 1):
            if i <= farthest:
                farthest = max(farthest, i + nums[i])
                
                if i == cur:
                    print(i, cur, farthest)
                    steps+=1
                    cur = farthest

        return steps
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**



