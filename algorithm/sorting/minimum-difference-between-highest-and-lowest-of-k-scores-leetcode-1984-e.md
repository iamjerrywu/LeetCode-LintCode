# Minimum Difference Between Highest and Lowest of K Scores \(LeetCode 1984\) \(E\)

## Problem

You are given a **0-indexed** integer array `nums`, where `nums[i]` represents the score of the `ith` student. You are also given an integer `k`.

Pick the scores of any `k` students from the array so that the **difference** between the **highest** and the **lowest** of the `k` scores is **minimized**.

Return _the **minimum** possible difference_.

**Example 1:**

```text
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
```

**Example 2:**

```text
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
```

**Constraints:**

* `1 <= k <= nums.length <= 1000`
* `0 <= nums[i] <= 105`

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        else:
            nums.sort()
            diff = float('inf')
            for i in range(0, len(nums) - k + 1):
                diff = min(diff, nums[i + k - 1] - nums[i])
            return diff
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O\(nlogn\)**
* **Space Complexity: O\(n\)**

