# Minimum Window Substring 32 (M)

## Problem

Given two strings `source` and `target`. Return the minimum substring of `source` which contains each char of `target`.

1. If there is no answer, return `""`.
2. You are guaranteed that the answer is unique.
3. `target` may contain duplicate char, while the answer need to contain at least the same number of that char.

Example

**Example 1:**

Input:

```
source = "abc"
target = "ac"
```

Output:

```
"abc"
```

Explanation:

"abc" is the minimum substring of source string which contains each char of target "ac".

**Example 2:**

Input:

```
source = "adobecodebanc"
target = "abc"
```

Output:

```
"banc"
```

Explanation:

"banc" is the minimum substring of source string which contains each char of target "abc".

**Example 3:**

Input:

```
source = "abc"
target = "aa"
```

Output:

```
""
```

Explanation:

No substring contains two 'a'.Challenge

O(n) time\


## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if not source or not target:
            return ''
        
        # m, n = len(target), len(source)

        target_counter, sub_counter = {}, {}
        for c in target:
            target_counter[c] = target_counter.get(c, 0) + 1
        
        j = 0
        matched_chars = 0
        start, substring_length = 0, float('inf')
        for i in range(len(source)):
            while j < len(source) and matched_chars < len(target_counter):
                sub_counter[source[j]] = sub_counter.get(source[j], 0) + 1
                if sub_counter[source[j]] == target_counter.get(source[j], 0):
                    matched_chars+=1
                j+=1
            
            if matched_chars == len(target_counter):
                if substring_length > j - i:
                    substring_length = j - i
                    start = i
                sub_counter[source[i]]-=1
                if sub_counter[source[i]] == target_counter.get(source[i], 0) - 1:
                    matched_chars-=1
        
        if substring_length == float('inf'):
            return ''
        return source[start : start + substring_length]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Sliding Window 2 (better)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        appears = Counter(t)
        ans_length = float('inf')
        ans = ''
        cnt = len(appears)
        
        start, end = 0, 0
        
        while end < len(s):
            while end < len(s) and cnt != 0:
                if s[end] in appears:
                    appears[s[end]]-=1
                    if appears[s[end]] == 0:
                        cnt-=1
                end+=1
            
            while start < end and cnt == 0:
                if ans_length > end - start:
                    ans_length = end - start
                    ans = s[start:end]
                
                if s[start] in appears:
                    appears[s[start]]+=1
                    if appears[s[start]] > 0:
                        cnt+=1
                    
                start+=1
        print(end, start)
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



## Solution **- Sliding Window 2 (better)**

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        appears = Counter(t)
        ans_length = float('inf')
        ans = ''
        cnt = len(appears)
        
        start = 0
        
        for end in range(len(s)):
            if cnt > 0:
                if s[end] in appears:
                    appears[s[end]]-=1
                    if appears[s[end]] == 0:
                        cnt-=1
            while start < (end + 1) and cnt == 0:
                if ans_length > end - start:
                    ans_length = end - start
                    ans = s[start:(end + 1)]
                if s[start] in appears:
                    appears[s[start]]+=1
                    if appears[s[start]] > 0:
                        cnt+=1
                start+=1
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

