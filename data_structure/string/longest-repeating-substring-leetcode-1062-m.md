# Longest Repeating Substring (LeetCode 1062) (M)

## Problem

Given a string `s`, find out the length of the longest repeating substring(s). Return `0` if no repeating substring exists.

&#x20;

**Example 1:**

```
Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.
```

**Example 2:**

```
Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
```

**Example 3:**

```
Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
```

**Example 4:**

```
Input: s = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
```

&#x20;

**Constraints:**

* The string `s` consists of only lowercase English letters from `'a'` - `'z'`.
* `1 <= s.length <= 1500`



## Solution - Brute Force (HastSet)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        substr_set = set()
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                substr = s[i:j + 1]
            
                if substr not in substr_set:
                    substr_set.add(substr)
                else:
                    ans = max(ans, len(substr))
        return ans
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n^3)**
  * Two for loop
  * The substr slicing: O(n)
* **Space Complexity:**

****

## Solution - Binary Search

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        start = 1
        end = len(s) - 1 # it's repeated, should not be len(s)
        
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if self.find_substring(mid, s):
                start = mid
            else:
                end = mid
        
        if self.find_substring(end, s):
            return end
        if self.find_substring(start, s):
            return start
        return 0
        
    def find_substring(self, length, s):
        substr_set = set()
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr not in substr_set:
                substr_set.add(substr)
            else:
                return True
        return False
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n^2logn)**
* **Space Complexity: O(n \* L)**

## Solution - Binary Search + Rolling Hash

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        nums = [ord(c) - ord('a') for c in s]
        
        start = 1
        end = len(s) - 1 # it's repeated, should not be len(s)
        
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if self.find_substring(mid, nums):
                start = mid
            else:
                end = mid
        
        if self.find_substring(end, nums):
            return end
        if self.find_substring(start, nums):
            return start
        return 0
        
    def find_substring(self, length, nums):        
        hash_set = set()
        
        hash_val = 0
        for i in range(length):
            hash_val = hash_val * 26 + nums[i]
        hash_set.add(hash_val)
        for i in range(1, len(nums) - length + 1):
            hash_val = hash_val * 26 - nums[i - 1] * 26 ** length + nums[i + length - 1] * 26 ** 0
            if hash_val in hash_set:
                return True
            hash_set.add(hash_val)
        return False

```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(nlogl)**
* **Space Complexity: O(n)**

## Solution - Binary Search + Rolling Hash



{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        nums = [ord(c) - ord('a') for c in s]
        
        start = 1
        end = len(s) - 1 # it's repeated, should not be len(s)
        
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if self.find_substring(mid, nums):
                start = mid
            else:
                end = mid
        
        if self.find_substring(end, nums):
            return end
        if self.find_substring(start, nums):
            return start
        return 0
        
    def find_substring(self, length, nums):        
        hash_set = set()
        
        hash_val = 0
        for i in range(length):
            hash_val = hash_val * 26 + nums[i]
        hash_set.add(hash_val)
        for i in range(1, len(nums) - length + 1):
            hash_val = hash_val * 26 - nums[i - 1] * 26 ** length + nums[i + length - 1] * 26 ** 0
            if hash_val in hash_set:
                return True
            hash_set.add(hash_val)
        return False

```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(nlogl)**
* **Space Complexity: O(n)**

****

****
