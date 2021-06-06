# Minimum Number of Flips to Make the Binary String Alternating \(LeetCode 1888\) \(M\)

## Problem

You are given a binary string `s`. You are allowed to perform two types of operations on the string in any sequence:

* **Type-1: Remove** the character at the start of the string `s` and **append** it to the end of the string.
* **Type-2: Pick** any character in `s` and **flip** its value, i.e., if its value is `'0'` it becomes `'1'` and vice-versa.

Return _the **minimum** number of **type-2** operations you need to perform_ _such that_ `s` _becomes **alternating**._

The string is called **alternating** if no two adjacent characters are equal.

* For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.

**Example 1:**

```text
Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
```

**Example 2:**

```text
Input: s = "010"
Output: 0
Explanation: The string is already alternating.
```

**Example 3:**

```text
Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
```

**Constraints:**

* `1 <= s.length <= 105`
* `s[i]` is either `'0'` or `'1'`.

[Discuss](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/discuss)  


## Solution - Sliding Window

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minFlips(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        s_double = s + s
        s_0 = "" # start with 0
        s_1 = "" # start with 1
        
        for i in range(len(s_double)):
            if i%2 == 0:
                s_0+='0'
                s_1+='1'
            else:
                s_0+='1'
                s_1+='0'
            
        res_0 = 0 # compare how many type 2 required for s_0
        res_1 = 0 # compare how many type 2 required for s_1
        res = 10**6
        
        for i in range(len(s_double)):
            if s_double[i] != s_0[i]:
                res_0+=1
            if s_double[i] != s_1[i]:
                res_1+=1
            
            # take care the tail
            if i >= n:
                if s_double[i - n] != s_0[i - n]:
                    res_0-=1
                if s_double[i - n] != s_1[i - n]:
                    res_1-=1
            if i >= n -1:
                res = min(res, res_0, res_1)
        
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

