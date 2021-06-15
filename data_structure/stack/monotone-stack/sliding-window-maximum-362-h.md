# Sliding Window Maximum 362 \(H\)

## Problem

Given an array of n integer with duplicate number, and a moving window\(size k\), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.Example

**Example 1:**

```text
Input:[1,2,7,7,8]3输出:[7,7,8]Explanation：At first the window is at the start of the array like this `[|1, 2, 7| ,7, 8]` , return the maximum `7`;then the window move one step forward.`[1, |2, 7 ,7|, 8]`, return the maximum `7`;then the window move one step forward again.`[1, 2, |7, 7, 8|]`, return the maximum `8`;
```

**Example 2:**

```text
Input:[1,2,3,1,2,3]5Output:[3,3]Explanation:At first, the state of the window is as follows: ` [,2,3,1,2,1 | , 3] `, a maximum of ` 3 `;And then the window to the right one. ` [1, | 2,3,1,2,3 |] `, a maximum of ` 3 `;
```

Challenge

o\(n\) time and O\(k\) memory

## Solution - Brute Force Enumeration

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            max_val = max(nums[i:i + k])
            res.append(max_val)
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* k\)**
* **Space Complexity: O\(n\)**

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

