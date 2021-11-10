# Longest Duplicate Substring (LeetCode 1044) (H)

## Problem



Given a string `s`, consider all _duplicated substrings_: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return **any** duplicated substring that has the longest possible length. If `s` does not have a duplicated substring, the answer is `""`.

&#x20;

**Example 1:**

```
Input: s = "banana"
Output: "ana"
```

**Example 2:**

```
Input: s = "abcd"
Output: ""
```

&#x20;

**Constraints:**

* `2 <= s.length <= 3 * 104`
* `s` consists of lowercase English letters.



## Solution - Binary Search

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        start = 1
        end = len(s) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if self.find_substring(mid, s):
                start = mid
            else:
                end = mid
        substr = self.find_substring(end, s)
        if substr:
            return substr
        return self.find_substring(start, s)
    
    def find_substring(self, length, s):
        substr_set = set()
        
        for i in range(0, len(s) - length + 1):
            substr = s[i:i + length]
            if substr in substr_set:
                return substr
            substr_set.add(substr)
        return ''
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Binary Search + Rolling Hash

This will end up LTE, since the values is too large causing overflow

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        start = 1
        end = len(s) - 1
        
        nums = [ord(c) - ord('a') for c in s] # transfer them into ascii value
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if self.find_substring(mid, s, nums):
                start = mid
            else:
                end = mid
        substr = self.find_substring(end, s, nums)
        if substr:
            return substr
        return self.find_substring(start, s, nums)
    
    def find_substring(self, length, s, nums):
        hash_set = set()
        hash_val = 0
        for i in range(length):
            hash_val = hash_val * 26 + nums[i]
        hash_set.add(hash_val)
        for i in range(1, len(s) - length + 1):
            hash_val = hash_val * 26 - nums[i - 1]*pow(26, length) + nums[i + length - 1]*pow(26, 0)
            if hash_val in hash_set:
                return s[i:i + length]
            hash_set.add(hash_val)
        return ''   
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Binary Search + Rolling Hash Mod

Require using two MOD to avoid overflow. Using one MOD is not enough, since the value is too large, will still end up hash collision (having two differnt substr but end up same hash value). To avoid this, can increase the MOD (but it will still overflow). Appropriate way to solve this is using two MOD here.



{% tabs %}
{% tab title="Python" %}
```python
# using two MOD here, since one MOD is not enough
# might end up hash collision
MOD = 2 ** 32
MOD2 = 2 ** 32 - 1
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        start = 1
        end = len(s) - 1
        
        nums = [ord(c) - ord('a') for c in s] # transfer them into ascii value
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if self.find_substring(mid, s, nums):
                start = mid
            else:
                end = mid
        substr = self.find_substring(end, s, nums)
        if substr:
            return substr
        return self.find_substring(start, s, nums)
    
    def find_substring(self, length, s, nums):
        hash_set = set()
        hash_val = 0
        hash_val2 = 0
        for i in range(length):
            hash_val = (hash_val * 26 + nums[i])%MOD
            hash_val2 = (hash_val2 * 26 + nums[i])%MOD2
        hash_set.add((hash_val, hash_val2))
        
        power = pow(26, length, MOD)
        power2 = pow(26, length, MOD2)
        for i in range(1, len(s) - length + 1):
            hash_val = (hash_val * 26 - nums[i - 1]*power + nums[i + length - 1]*pow(26, 0))%MOD
            hash_val2 = (hash_val2 * 26 - nums[i - 1]*power2 + nums[i + length - 1]*pow(26, 0))%MOD2
            
            if (hash_val, hash_val2) in hash_set:
                return s[i:i + length]
            hash_set.add((hash_val, hash_val2))
        return ''
        
        
    
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
