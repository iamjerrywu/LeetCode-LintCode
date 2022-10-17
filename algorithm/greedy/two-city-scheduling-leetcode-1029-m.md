# Two City Scheduling (LeetCode 1029) (M)

## Problem

****

A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCosti, bCosti]`, the cost of flying the `ith` person to city `a` is `aCosti`, and the cost of flying the `ith` person to city `b` is `bCosti`.

Return _the minimum cost to fly every person to a city_ such that exactly `n` people arrive in each city.

&#x20;

**Example 1:**

<pre><code>Input: costs = [[10,20],[30,200],[400,50],[30,20]]
<strong>Output:
</strong> 110
<strong>Explanation: 
</strong>The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.</code></pre>

**Example 2:**

<pre><code>Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
<strong>Output:
</strong> 1859</code></pre>

**Example 3:**

<pre><code>Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
<strong>Output:
</strong> 3086</code></pre>

&#x20;

**Constraints:**

* `2 * n == costs.length`
* `2 <= costs.length <= 100`
* `costs.length` is even.
* `1 <= aCosti, bCosti <= 1000`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        # find out those who are more worthy to send to city B than city A
        b_cost = []
        for i, c_list in enumerate(costs):
            b_cost.append([c_list[1] - c_list[0], i])
        b_cost.sort()
        print(b_cost)
        ans = 0
        for i, v_list in enumerate(b_cost):
            if i < len(costs)//2:
                ans+=costs[v_list[1]][1]
            else:
                ans+=costs[v_list[1]][0]
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
