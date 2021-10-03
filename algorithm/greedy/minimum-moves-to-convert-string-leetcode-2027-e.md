# Minimum Moves to Convert String \(LeetCode 2027\) \(E\)

## Problem

A **move** is defined as selecting **three** **consecutive characters** of `s` and converting them to `'O'`. Note that if a move is applied to the character `'O'`, it will stay the **same**.

Return _the **minimum** number of moves required so that all the characters of_ `s` _are converted to_ `'O'`.

**Example 1:**

```text
Input: s = "XXX"
Output: 1
Explanation: XXX -> OOO
We select all the 3 characters and convert them in one move.
```

**Example 2:**

```text
Input: s = "XXOX"
Output: 2
Explanation: XXOX -> OOOX -> OOOO
We select the first 3 characters in the first move, and convert them to 'O'.
Then we select the last 3 characters and convert them so that the final string contains all 'O's.
```

**Example 3:**

```text
Input: s = "OOOO"
Output: 0
Explanation: There are no 'X's in s to convert.
```

**Constraints:**

* `3 <= s.length <= 1000`
* `s[i]` is either `'X'` or `'O'`.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        cnt = 0
        while i < len(s):
            if s[i] == 'O':
                i+=1
            else:
                cnt+=1
                i+=3
        return cnt
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:**

