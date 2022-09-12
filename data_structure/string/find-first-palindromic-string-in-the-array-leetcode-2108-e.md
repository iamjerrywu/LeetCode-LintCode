# Find First Palindromic String in the Array (LeetCode 2108) (E)

## Problem

****

Given an array of strings `words`, return _the first **palindromic** string in the array_. If there is no such string, return _an **empty string** _ `""`.

A string is **palindromic** if it reads the same forward and backward.

&#x20;

**Example 1:**

<pre><code>Input: words = ["abc","car","ada","racecar","cool"]
<strong>Output:
</strong> "ada"
<strong>Explanation:
</strong> The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.</code></pre>

**Example 2:**

<pre><code>Input: words = ["notapalindrome","racecar"]
<strong>Output:
</strong> "racecar"
<strong>Explanation:
</strong> The first and only string that is palindromic is "racecar".</code></pre>

**Example 3:**

<pre><code>Input: words = ["def","ghi"]
<strong>Output:
</strong> ""
<strong>Explanation:
</strong> There are no palindromic strings, so the empty string is returned.</code></pre>

&#x20;

**Constraints:**

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 100`
* `words[i]` consists only of lowercase English letters.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""
    
    def is_palindrome(self, word):
        left, right = 0, len(word) - 1
        
        while left < right:
            if word[left] != word[right]:
                return False
            left+=1
            right-=1
        return True
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

****
