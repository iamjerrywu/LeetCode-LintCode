# Top K Frequent Words (LeetCode 692) (M)



## Problem

Given an array of strings `words` and an integer `k`, return _the _`k`_ most frequent strings_.

Return the answer **sorted** by **the frequency** from highest to lowest. Sort the words with the same frequency by their **lexicographical order**.

&#x20;

**Example 1:**

```
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
```

**Example 2:**

```
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
```

&#x20;

**Constraints:**

* `1 <= words.length <= 500`
* `1 <= words[i] <= 10`
* `words[i]` consists of lowercase English letters.
* `k` is in the range `[1, The number of `**`unique`**` words[i]]`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        
        word_list = [[k, v] for k, v in count.items()]
        
        # first sort with appearance times, then sort by alphabatical orders
        word_list.sort(key = lambda w:(-w[1], w[0]))
        
        ans = [word for word, times in word_list[:k]]
        return ans
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
