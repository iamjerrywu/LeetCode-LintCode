# Custom Sort String (LeetCode 791) (M)

## Problem

You are given two strings order and s. All the words of `order` are **unique** and were sorted in some custom order previously.

Permute the characters of `s` so that they match the order that `order` was sorted. More specifically, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string.

Return _any permutation of_ `s` _that satisfies this property_.

&#x20;

**Example 1:**

```
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
```

**Example 2:**

```
Input: order = "cbafg", s = "abcd"
Output: "cbad"
```

&#x20;

**Constraints:**

* `1 <= order.length <= 26`
* `1 <= s.length <= 200`
* `order` and `s` consist of lowercase English letters.
* All the characters of `order` are **unique**.



## Solution - HashMap

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        exist = collections.defaultdict(int)
        not_exist = collections.defaultdict(int)
        
        order_set = set(order)
        
        for c in s:
            if c in order_set:
                exist[c]+=1
            else:
                not_exist[c]+=1
        ans = ""
        for c in order:
            if c in exist:
                ans+=c * exist[c]
        
        for k, v in not_exist.items():
            ans+=k * v
        return ans
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

* **Time Complexity:**
* **Space Complexity:**

