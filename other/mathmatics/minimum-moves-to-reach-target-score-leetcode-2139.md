# Minimum Moves to Reach Target Score (LeetCode 2139)

## Problem

You are playing a game with integers. You start with the integer `1` and you want to reach the integer `target`.

In one move, you can either:

* **Increment** the current integer by one (i.e., `x = x + 1`).
* **Double** the current integer (i.e., `x = 2 * x`).

You can use the **increment** operation **any** number of times, however, you can only use the **double** operation **at most** `maxDoubles` times.

Given the two integers `target` and `maxDoubles`, return _the minimum number of moves needed to reach_ `target` _starting with_ `1`.

&#x20;

**Example 1:**

<pre><code>Input: target = 5, maxDoubles = 0
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> Keep incrementing by 1 until you reach target.
</code></pre>

**Example 2:**

<pre><code>Input: target = 19, maxDoubles = 2
<strong>Output:
</strong> 7
<strong>Explanation:
</strong> Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19
</code></pre>

**Example 3:**

<pre><code>Input: target = 10, maxDoubles = 4
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10
</code></pre>

&#x20;

**Constraints:**

* `1 <= target <= 109`
* `0 <= maxDoubles <= 100`



## Solution - Greedy

Greedy thinking that as long as there's double method, use double. If target is not divided by 2, use increatment method.

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 1:
            if maxDoubles:
                if target%2:
                    target-=1
                    ans+=1
                else:
                    target//=2
                    maxDoubles-=1
                    ans+=1
            else:
                ans+=target - 1
                break
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

* **Time Complexity:**&#x20;
* **Space Complexity:**

