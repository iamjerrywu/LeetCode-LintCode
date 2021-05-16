# Minimum Number of Swaps to Make the Binary String Alternating \(LeetCode 1864\) \(M\)

## Problem

Given a binary string `s`, return _the **minimum** number of character swaps to make it **alternating**, or_ `-1` _if it is impossible._

The string is called **alternating** if no two adjacent characters are equal. For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.

Any two characters may be swapped, even if they are **not adjacent**.

**Example 1:**

```text
Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
```

**Example 2:**

```text
Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
```

**Example 3:**

```text
Input: s = "1110"
Output: -1
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s[i]` is either `'0'` or `'1'`.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minSwaps(self, s: str) -> int:
        count = Counter(s)
        
        # impossible to make it alternating string
        if abs(count['0'] - count['1']) > 1:
            return -1
        
        zero_start = False
        if count['0'] > count['1']:
            return self.swap_cnt(s, zero_start = True)
        elif count['0'] < count['1']:
            return self.swap_cnt(s, zero_start = False)
        else: # count['0'] == count['1']:
            return min(self.swap_cnt(s, zero_start = True), self.swap_cnt(s, zero_start = False))
    
    def swap_cnt(self, s, zero_start):
        cnt = 0
        for i in range(len(s)):
            if zero_start:
                if i%2 == 0 and s[i] != '0' or i%2 == 1 and s[i] != '1':
                    cnt+=1
            else:
                if i%2 == 0 and s[i] != '1' or i%2 == 1 and s[i] != '0':
                    cnt+=1
        return cnt//2
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

