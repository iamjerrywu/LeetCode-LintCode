# Minimum Size Subarray Sum 406 \(M\)

## Problem

Given an array of `n` positive integers and a positive integer `s`, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.Example

**Example 1:**

```text
Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**

```text
Input: [1, 2, 3, 4, 5], s = 100
Output: -1
```

Challenge

If you have figured out the O\(nlog n\) solution, try coding another solution of which the time complexity is O\(n\).

## Solution - Prefix Sum

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        ans = float('inf')
        for start in range(len(nums)):
            sum_val = 0
            for end in range(start, len(nums)):
                sum_val+=nums[end]
                if sum_val >= s:
                    ans = min(ans, end - start + 1)
        return ans if ans != float('inf') else -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(1\)**

## Solution - Prefix Sum \(2\)

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

## 

## Solution - Prefix Sum + Binary Search

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

## Solution - Two Pointers

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

