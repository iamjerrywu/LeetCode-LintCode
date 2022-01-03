# Find the Town Judge (LeetCode 997) (E)

## Problem

****

In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties **1** and **2**.

You are given an array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`.

Return _the label of the town judge if the town judge exists and can be identified, or return_ `-1` _otherwise_.

&#x20;

**Example 1:**

```
Input: n = 2, trust = [[1,2]]
Output: 2
```

**Example 2:**

```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

**Example 3:**

```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

&#x20;

**Constraints:**

* `1 <= n <= 1000`
* `0 <= trust.length <= 104`
* `trust[i].length == 2`
* All the pairs of `trust` are **unique**.
* `ai != bi`
* `1 <= ai, bi <= n`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n == 1 and not trust:
            return 1
        
        trusted = [0] * (n + 1)
        trust_others = [0] * (n + 1)
        for p1, p2 in trust:
            trusted[p2]+=1
            trust_others[p1]+=1
        for i, val in enumerate(trusted):
            if val == n - 1 and trust_others[i] == 0:
                return i
        return -1
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
