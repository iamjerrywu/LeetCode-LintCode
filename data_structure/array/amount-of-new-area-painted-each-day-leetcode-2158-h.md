# Amount of New Area Painted Each Day (LeetCode 2158) (H)

## Problem

There is a long and thin painting that can be represented by a number line. You are given a **0-indexed** 2D integer array `paint` of length `n`, where `paint[i] = [starti, endi]`. This means that on the `ith` day you need to paint the area **between** `starti` and `endi`.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most **once**.

Return _an integer array_ `worklog` _of length_ `n`_, where_ `worklog[i]` _is the amount of **new** area that you painted on the_ `ith` _day._

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-16-16-diagram-drawio-diagrams-net.png)

<pre><code>Input: paint = [[1,4],[4,7],[5,8]]
<strong>Output:
</strong> [3,3,1]
<strong>Explanation:
</strong>On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1. </code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-17-45-diagram-drawio-diagrams-net.png)

<pre><code>Input: paint = [[1,4],[5,8],[4,7]]
<strong>Output:
</strong> [3,3,1]
<strong>Explanation:
</strong>On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 5 and 8.
The amount of new area painted on day 1 is 8 - 5 = 3.
On day 2, paint everything between 4 and 5.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 5 - 4 = 1. </code></pre>

**Example 3:**

![](https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-19-49-diagram-drawio-diagrams-net.png)

<pre><code>Input: paint = [[1,5],[2,4]]
<strong>Output:
</strong> [4,0]
<strong>Explanation:
</strong>On day 0, paint everything between 1 and 5.
The amount of new area painted on day 0 is 5 - 1 = 4.
On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
The amount of new area painted on day 1 is 0.</code></pre>

&#x20;

**Constraints:**

* `1 <= paint.length <= 105`
* `paint[i].length == 2`
* `0 <= starti < endi <= 5 * 104`

Accepted18,726Submissions\




## Solution - Greedy

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        
        #[1, 4]
        # -> {1 : 4}
        # -> {2 : 4}
        # -> {3 : 4}
        rec = dict()
        ans = []
        for p_s, p_e in paint:
            cnt = 0
            while p_s < p_e:
                if p_s in rec:
                    prev_e = rec[p_s]
                    rec[p_s] = max(rec[p_s], p_e)
                    p_s = prev_e
                else:
                    rec[p_s] = p_e
                    p_s+=1
                    cnt+=1
            ans.append(cnt)
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
