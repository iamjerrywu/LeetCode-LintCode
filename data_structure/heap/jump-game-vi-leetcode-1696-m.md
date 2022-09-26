# Jump Game VI (LeetCode 1696) (M)

## Problem

****

You are given a **0-indexed** integer array `nums` and an integer `k`.

You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going outside the boundaries of the array. That is, you can jump from index `i` to any index in the range `[i + 1, min(n - 1, i + k)]` **inclusive**.

You want to reach the last index of the array (index `n - 1`). Your **score** is the **sum** of all `nums[j]` for each index `j` you visited in the array.

Return _the **maximum score** you can get_.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,-1,-2,4,-7,3], k = 2
<strong>Output:
</strong> 7
<strong>Explanation:
</strong> You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.</code></pre>

**Example 2:**

<pre><code>Input: nums = [10,-5,-2,4,0,3], k = 3
<strong>Output:
</strong> 17
<strong>Explanation:
</strong> You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.</code></pre>

**Example 3:**

<pre><code>Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
<strong>Output:
</strong> 0</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length, k <= 105`
* `-104 <= nums[i] <= 104`



##

## Solution - DP (TLE)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums) 
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[max(0, i - k):i])
        return dp[-1]
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

## Solution - Heap&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        max_val = nums[0]
        heap = []
        heapq.heappush(heap, (-nums[0], 0))
        for i in range(1, len(nums)):
            while heap[0][1] < i - k:
                heapq.heappop(heap)
            max_val = heap[0][0] - nums[i]
            heapq.heappush(heap, (max_val, i))
            if i == len(nums) - 1:
                return -(max_val)
        return nums[0]
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

