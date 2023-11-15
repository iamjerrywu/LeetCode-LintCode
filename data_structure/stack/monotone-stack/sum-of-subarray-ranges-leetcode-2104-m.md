# Sum of Subarray Ranges (LeetCode 2104) (M)

## Problem

You are given an integer array `nums`. The **range** of a subarray of `nums` is the difference between the largest and smallest element in the subarray.

Return _the **sum of all** subarray ranges of_ `nums`_._

A subarray is a contiguous **non-empty** sequence of elements within an array.

&#x20;

**Example 1:**

<pre><code>Input: nums = [1,2,3]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
</code></pre>

**Example 2:**

<pre><code>Input: nums = [1,3,3]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
</code></pre>

**Example 3:**

<pre><code>Input: nums = [4,-2,-3,4,1]
<strong>Output:
</strong> 59
<strong>Explanation:
</strong> The sum of all subarray ranges of nums is 59.
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 1000`
* `-109 <= nums[i] <= 109`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # ans = sum(max(subarr)) - sum(min(subarr))
        
        # monotonic increasing stack
        inc_stack = []
        min_sum = 0
        for nxt_smaller in range(len(nums) + 1):
            while inc_stack and (nxt_smaller == len(nums) or nums[nxt_smaller] < nums[inc_stack[-1]]):
                cur = inc_stack.pop()
                prev_smaller = inc_stack[-1] if inc_stack else -1
                min_sum+=(nxt_smaller - cur) * (cur - prev_smaller) * nums[cur]
            inc_stack.append(nxt_smaller)
        
        # monotonic decreasing stack 
        dec_stack = []
        max_sum = 0
        for nxt_larger in range(len(nums) + 1):
            while dec_stack and (nxt_larger == len(nums) or nums[nxt_larger] > nums[dec_stack[-1]]):
                cur = dec_stack.pop()
                prev_larger = dec_stack[-1] if dec_stack else -1
                max_sum+=(nxt_larger - cur) * (cur - prev_larger) * nums[cur]
            dec_stack.append(nxt_larger)
        
        return max_sum - min_sum
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

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

