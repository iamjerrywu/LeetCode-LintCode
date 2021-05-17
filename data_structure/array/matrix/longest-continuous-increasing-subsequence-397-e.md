# Longest Continuous Increasing Subsequence 397 \(E\)

## Problem

Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

* Can be from right to left or from left to right.
* Indices of the integers in the subsequence should be continuous.

Example

**Example 1:**

```text
Input: [5, 4, 2, 1, 3]
Output: 4
Explanation:
For [5, 4, 2, 1, 3], the LICS  is [5, 4, 2, 1], return 4.
```

**Example 2:**

```text
Input: [5, 1, 2, 3, 4]
Output: 4
Explanation:
For [5, 1, 2, 3, 4], the LICS  is [1, 2, 3, 4], return 4.
```

Challenge

O\(n\) time and O\(1\) extra space.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        
        longest, inc, dec = 0, 1, 1
        for i in range(len(A)):
            if A[i] > A[i - 1]:
                inc +=1
                dec = 1
            elif A[i] < A[i - 1]:
                dec +=1
                inc = 1
            else:
                inc = 1
                dec = 1
            longest = max(longest, max(inc, dec))
        return longest
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

