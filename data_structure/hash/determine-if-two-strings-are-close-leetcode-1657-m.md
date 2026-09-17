# Determine if Two Strings Are Close (LeetCode 1657) (M)

## Problem

Two strings are considered **close** if you can attain one from the other using the following operations:

* Operation 1: Swap any two **existing** characters.
  * For example, `abcde -> aecdb`
* Operation 2: Transform **every** occurrence of one **existing** character into another **existing** character, and do the same with the other character.
  * For example, `aacabb -> bbcbaa` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` _if_ `word1` _and_ `word2` _are **close**, and_ `false` _otherwise._

&#x20;

**Example 1:**

<pre><code><strong>Input: word1 = "abc", word2 = "bca"
</strong><strong>Output: true
</strong><strong>Explanation: You can attain word2 from word1 in 2 operations.
</strong>Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
</code></pre>

**Example 2:**

<pre><code><strong>Input: word1 = "a", word2 = "aa"
</strong><strong>Output: false
</strong><strong>Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
</strong></code></pre>

**Example 3:**

<pre><code><strong>Input: word1 = "cabbba", word2 = "abbccc"
</strong><strong>Output: true
</strong><strong>Explanation: You can attain word2 from word1 in 3 operations.
</strong>Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
</code></pre>

&#x20;

**Constraints:**

* `1 <= word1.length, word2.length <= 10`<sup>`5`</sup>
* `word1` and `word2` contain only lowercase English letters.



## Solution

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
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length()) return false;

        // use array instead of hashmap, reduce hashing, heap allocation
        array<int, 26> freq1;
        array<int, 26> freq2;

        for (char c : word1) freq1[c - 'a']+=1;
        for (char c : word2) freq2[c - 'a']+=1;
        
        // check if char are the same
        for (int i = 0; i < 26; i++) {
            bool hasChar1 = freq1[i] > 0;
            bool hasChar2 = freq2[i] > 0;
            if (hasChar1 != hasChar2) return false;
        }

        // sort both to them
        sort(freq1.begin(), freq1.end());
        sort(freq2.begin(), freq2.end());
        
        return freq1 == freq2;

    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
  * n = max(word1.length, word2.length)
* **Space Complexity: O(n)**
