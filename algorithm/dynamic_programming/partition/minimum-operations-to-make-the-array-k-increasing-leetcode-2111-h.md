# Minimum Operations to Make the Array K-Increasing (LeetCode 2111) (H)

## Problem



Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A **subsequence** is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.

&#x20;

**Example 1:**

<pre><code>Input: nums = [10,9,2,5,3,7,101,18]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</code></pre>

**Example 2:**

<pre><code>Input: nums = [0,1,0,3,2,3]
<strong>Output:
</strong> 4
</code></pre>

**Example 3:**

<pre><code>Input: nums = [7,7,7,7,7,7,7]
<strong>Output:
</strong> 1
</code></pre>

&#x20;

**Constraints:**

* `1 <= nums.length <= 2500`
* `-104 <= nums[i] <= 104`



## Solution&#x20;

**Idea**

* If `k = 1`, we need to find the minimum number of operations to make the whole array non-decreasing.
* If `k = 2`, we need to make:
  * newArr1: Elements in index \[0, 2, 4, 6...] are non-decreasing.
  * newArr2: Elements in index \[1, 3, 5, 7...] are non-decreasing.
* If `k = 3`, we need to make:
  * newArr1: Elements in index \[0, 3, 6, 9...] are non-decreasing.
  * newArr2: Elements in index \[1, 4, 7, 10...] are non-decreasing.
  * newArr3: Elements in index \[2, 5, 8, 11...] are non-decreasing.
* Since **Elements in newArrs are independent**, we just need to **find the minimum of operations to make `K` newArr non-decreasing**.
* To **find the minimum of operations to make an array non-decreasing**,
  * Firstly, we count **Longest Non-Decreasing Subsequence** in that array.
  * Then the result is `len(arr) - longestNonDecreasing(arr)`, because we only need to change elements not in the **Longest Non-Decreasing Subsequence**.
  * For example: `newArr = [18, 8, 8, 3, 9]`, the longest non-decreasing subsequence is `[-, 8, 8, -, 9]` and we just need to change the array into `[8, 8, 8, 9, 9]` by changing `18 -> 8`, `3 -> 9`.

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return 0

        lis = [float('inf')] * (len(nums) + 1)
        lis[0] = -float('inf') 

        longest = 0
        for num in nums:
            print(lis)
            index = self.first_gte(lis, num)
            print(index, num)
            lis[index] = num
            longest = max(longest, index)
        
        return longest

    def first_gte(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start
        return end


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

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(n)**
