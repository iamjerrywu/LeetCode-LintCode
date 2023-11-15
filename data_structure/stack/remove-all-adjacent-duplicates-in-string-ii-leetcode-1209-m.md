# Remove All Adjacent Duplicates In String II (LeetCode 1209) (M)

## Problem

You are given a string `s` and an integer `k`, a `k` **duplicate removal** consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make `k` **duplicate removals** on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

&#x20;

**Example 1:**

```
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
```

**Example 2:**

```
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
```

**Example 3:**

```
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
```

&#x20;

**Constraints:**

* `1 <= s.length <= 105`
* `2 <= k <= 104`
* `s` only contains lower case English letters.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] +=1
            elif not stack or stack[-1][0] != c:
                stack.append([c, 1])    
            # check in the end of round if length of same character >= k
            # for this prob, once reach k, should pop out immediately
            if stack[-1][1] >= k:
                stack.pop()
        ans = ''
        for c, cnt in stack:
            ans+=c * cnt
        return ans
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

