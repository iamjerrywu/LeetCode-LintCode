# Triangle Count 382 (M)

## Problem

Description

Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?Example

**Example 1:**

```
Input: [3, 4, 6, 7]
Output: 3
Explanation:
They are (3, 4, 6), 
         (3, 6, 7),
         (4, 6, 7)
```

**Example 2:**

```
Input: [4, 4, 4, 4]
Output: 4
Explanation:
Any three numbers can form a triangle. 
So the answer is C(3, 4) = 4
```

## Solution

![](<../../../../.gitbook/assets/Screen Shot 2021-04-22 at 11.48.54 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S.sort()
        cnt = 0
        for i in range(len(S)):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    cnt += right - left
                    right-=1
                else:
                    left+=1
        return cnt
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
