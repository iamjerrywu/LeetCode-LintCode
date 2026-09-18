# Removing Starts From a String (LeetCode 2390) (M)

## Problem

You are given a string `s`, which contains stars `*`.

In one operation, you can:

* Choose a star in `s`.
* Remove the closest **non-star** character to its **left**, as well as remove the star itself.

Return _the string after **all** stars have been removed_.

**Note:**

* The input will be generated such that the operation is always possible.
* It can be shown that the resulting string will always be unique.

&#x20;

**Example 1:**

<pre><code><strong>Input: s = "leet**cod*e"
</strong><strong>Output: "lecoe"
</strong><strong>Explanation: Performing the removals from left to right:
</strong><strong>- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
</strong><strong>- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
</strong><strong>- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
</strong>There are no more stars, so we return "lecoe".
</code></pre>

**Example 2:**

<pre><code><strong>Input: s = "erase*****"
</strong><strong>Output: ""
</strong><strong>Explanation: The entire string is removed, so we return an empty string.
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 10`<sup>`5`</sup>
* `s` consists of lowercase English letters and stars `*`.
* The operation above can be performed on `s`.



## Solution - Stack&#x20;

This is the standard, clean solution expected in most general software engineering interviews. By using `ans.reserve(s.size())` and treating the string like a stack with `push_back()` and `pop_back()`, you write highly readable, bug-resistant code. The trade-off is the unavoidable second heap allocation to store the result, which doubles your memory footprint for this specific operation.

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    string removeStars(string s) {
        string ans;
        for (char c : s) {
            if (c == '*') {
                ans.pop_back();
                continue;
            }
            ans.push_back(c);
        }
        return ans;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

## Solution - Two Pointers

This is the Staff-level systems and infrastructure solution. Because the function signature `string removeStars(string s)` passes the input by value, C++ is already handing you a freshly allocated, mutable copy of the string. By using a read pointer and a write pointer to overwrite characters in that exact same buffer, and then finishing with `s.resize()`, you execute the entire algorithm without requesting a single extra byte of heap memory. This demonstrates a deep understanding of standard library memory management and zero-copy principles.

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    string removeStars(string s) {
        int l = 0;

        for (int r = 0; r < s.length(); r++) {
            if (s[r] == '*') l--;
            else s[l++] = s[r];
        }
        s.resize(l);
        return s;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
