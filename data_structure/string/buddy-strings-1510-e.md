# Buddy Strings 1510 \(E\)

## Problem

Given two strings `A` and `B` of lowercase letters, return true if and only if we can swap two letters in `A` so that the result equals `B`.Otherwise, return false.

1.`0 <= A.length <= 20000`  
2.`0 <= A.length <= 20000`  
3.`A` and `B` consist only of lowercase letters.Example

**Example 1:**

```text
Input: A = "ab", B = "ba"
Output: true
```

**Example 2:**

```text
Input: A = "ab", B = "ab"
Output: false
```

**Example 3:**

```text
Input: A = "aa", B = "aa"
Output: true
```

**Example 4:**

```text
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
```

**Example 5:**

```text
Input: A = "", B = "aa"
Output: false
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: string A
    @param B: string B
    @return: bool
    """
    def buddyStrings(self, A, B):
        # Write your code here
        
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True
        diff = [(a, b) for a, b in zip(A, B) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]
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

