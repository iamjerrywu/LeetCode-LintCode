# K-Similar Strings (LeetCode 854) (H)



## Problem



Strings `s1` and `s2` are `k`**-similar** (for some non-negative integer `k`) if we can swap the positions of two letters in `s1` exactly `k` times so that the resulting string equals `s2`.

Given two anagrams `s1` and `s2`, return the smallest `k` for which `s1` and `s2` are `k`**-similar**.

&#x20;

**Example 1:**

```
Input: s1 = "ab", s2 = "ba"
Output: 1
```

**Example 2:**

```
Input: s1 = "abc", s2 = "bca"
Output: 2
```

**Example 3:**

```
Input: s1 = "abac", s2 = "baca"
Output: 2
```

**Example 4:**

```
Input: s1 = "aabc", s2 = "abca"
Output: 2
```

&#x20;

**Constraints:**

* `1 <= s1.length <= 20`
* `s2.length == s1.length`
* `s1` and `s2` contain only lowercase letters from the set `{'a', 'b', 'c', 'd', 'e', 'f'}`.
* `s2` is an anagram of `s1`.

## Solution - BFS (Brute Force) (TLE)

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        visited = set()
        queue = collections.deque()
        
        queue.append(s1)
        ans = 0
        while queue:    
            for _ in range(len(queue)):
                cur_s = queue.popleft()
                if cur_s == s2:
                    return ans
                # Literally swap any two indexes
                for i in range(len(cur_s) - 1):
                    for j in range(i + 1, len(cur_s)):
                        new_s = cur_s[:i] + cur_s[j] + cur_s[i + 1:j] + cur_s[i] + cur_s[j + 1:]
                        if new_s not in visited:
                            queue.append(new_s)
                            visited.add(new_s)
            ans+=1
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**



## Solution - BFS (Prunning)

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        visited = set()
        queue = collections.deque()
        
        queue.append(s1)
        ans = 0
        while queue:    
            for _ in range(len(queue)):
                cur_s = queue.popleft()
                if cur_s == s2:
                    return ans
                i = 0
                # prunning, if cur_s[i] == str2[i], skip
                while i < len(cur_s) and cur_s[i] == s2[i]:
                    i+=1
                
                # only swap cur_s[i]/cur_s[j], if cur_s[j] != str2[j]
                # and after swapping can make cur_s[j] == str2[j]
                for j in range(i, len(cur_s)):
                    if cur_s[j] == s2[i] and cur_s[j] != s2[j]:
                        new_s = cur_s[:i] + cur_s[j] + cur_s[i + 1:j] + cur_s[i] + cur_s[j + 1:]
                        if new_s not in visited:
                            queue.append(new_s)
                            visited.add(new_s)
            ans+=1
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**



