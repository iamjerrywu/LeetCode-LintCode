# Longest Substring Without Repeating Characters 384 (M)

## Problem

Description

Given a string, find the length of the longest substring without repeating characters.Example

**Example 1:**

```
Input: "abcabcbb"
Output: 3
Explanation: The longest substring is "abc".
```

**Example 2:**

```
Input: "bbbbb"
Output: 1
Explanation: The longest substring is "b".
```

Challenge

time complexity O(n)

## Solution - Two Pointer and Set

Two pointer that one act as start point, and the other would traverse `s` and stop until encounter repetitive characters. Use set to record unique characters, and once move the start pointer to next step, remove the repetitive character inside.&#x20;



### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        unique = set()
        longest, j = 0, 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in unique:
                unique.add(s[j])
                j+=1
            longest = max(longest, j - i)
            unique.remove(s[i])
        return longest
            

```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() < 2) return s.length();
        
        int r = 0;
        set<char> rec;
        int ans = 0;
        for (int l = 0; l < s.length(); l++) {
            while ((r < s.length()) && (rec.count(s[r]) == 0)) {
                rec.insert(s[r]);
                r+=1;
            }
            ans = max(ans, r - l);
            rec.erase(s[l]);
        }
        return ans;
        
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n)**



## Solution - Hashmap

Use Hashmap to recorded the visited characters, and update the start pointer to the position of the latest visited character's previous existed location + 1.&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        seen = {}
        start, longest = 0, 0
        for i, c in enumerate(s):
            if seen.get(c, -1) >= start:
                start = seen[c] + 1
            else:
                longest = max(longest, i - start + 1)
            seen[c] = i
        return longest
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

## Solution - Array (Best)

We can simply use Array since the character amounts are fix, most likely just 128 in ASCII code. Also, we can simply move the left pointer directry to the alreadty seen character location, instead of +1, +1 moving.

### Code

{% tabs %}
{% tab title="python" %}
```python
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        // since ASII character only has 128
        std::vector<int> seen(128, -1);

        if (s.length() <= 1) return s.length();
        int l = 0, ans = 0;
        for (int r = 0; r < s.length(); r++) {
            if (seen[s[r]] >= l) {
                // we can simply move the left pointer to the last seen index
                l = seen[s[r]] + 1;
            }
            seen[s[r]] = r;

            ans = std::max(ans, r - l + 1);
        }
        return ans;

    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

