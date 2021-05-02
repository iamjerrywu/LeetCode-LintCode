---
description: Weekly Contest
---

# Splitting a String Into Descending Consecutive Values \(LeetCode 1849\) \(M\) \(

## Problem

You are given a string `s` that consists of only digits.

Check if we can split `s` into **two or more non-empty substrings** such that the **numerical values** of the substrings are in **descending order** and the **difference** between numerical values of every two **adjacent** **substrings** is equal to `1`.

* For example, the string `s = "0090089"` can be split into `["0090", "089"]` with numerical values `[90,89]`. The values are in descending order and adjacent values differ by `1`, so this way is valid.
* Another example, the string `s = "001"` can be split into `["0", "01"]`, `["00", "1"]`, or `["0", "0", "1"]`. However all the ways are invalid because they have numerical values `[0,1]`, `[0,1]`, and `[0,0,1]` respectively, all of which are not in descending order.

Return `true` _if it is possible to split_ `s`​​​​​​ _as described above, or_ `false` _otherwise._

A **substring** is a contiguous sequence of characters in a string.

**Example 1:**

```text
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.
```

**Example 2:**

```text
Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.
```

**Example 3:**

```text
Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.
```

**Example 4:**

```text
Input: s = "10009998"
Output: true
Explanation: s can be split into ["100", "099", "98"] with numerical values [100,99,98].
The values are in descending order with adjacent values differing by 1.
```

**Constraints:**

* `1 <= s.length <= 20`
* `s` only consists of digits.

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def splitString(self, s: str) -> bool:
        return self.dfs(s, 0, None, None)
    def dfs(self, s, index, cur, prev):
        # prunning, can return if False
        if prev != None and cur != None and prev - cur != 1:
            return False
        if prev != None and cur != None and index == len(s):
            return True
        prev = cur
        # move 1 ~ (len(s) - index) steps 
        for i in range(1, len(s) - index + 1):
            # prunning, can return if True
            if self.dfs(s, index + i, int(s[index:index + i]), prev):
                return True
        # return False if already find all combinations
        return False
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

