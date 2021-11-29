# Bulb Switcher 319 (M)

## Problem

There are `n` bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the `ith` round, you toggle every `i` bulb. For the `nth` round, you only toggle the last bulb.

Return _the number of bulbs that are on after `n` rounds_.

**Example 1:**![](https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg)

```
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
```

**Example 2:**

```
Input: n = 0
Output: 0
```

**Example 3:**

```
Input: n = 1
Output: 1
```

**Constraints:**

* `0 <= n <= 109`

## Solution&#x20;

Before we take a jump to the solution, let's first try to clear out what exactly the problem is talking about:

* every i-th distance you switch the bulb to the opposite state (from on to off, or from off to on); actually suppose the bulbs are labelled from 1 to n then the every second bulb will mean that 2, 4, 6, 8, ... all even numbers less than n; while every third bulb will be 3, 6, 9, 12, ... all multiples of 3 that is less than n and so on;
* since the bulb will only have two different states - on or off, the result will be quite clear now; odd switching operations will result in bulb-on state (since original state is bulb-off) while even switching operations will give us bulb-off state;

Now the purpose here is clear searching for the **odd-operation numbers**:

* as for primes, they only have 1 and itself as their factors, even-operation numbers;
* as for non-primes, normally they will have different pairs of factors like 12 whose factors are (1, 12), (3, 4), (2, 6) - 6 different factors, also even-operation numbers;
* but among non-primes, there are some special numbers, perfect square numbers like 9 whose factors are (1, 9) and (3, 3) - odd-operation numbers, which means there will be only three different numbers that will affect the current bulb and result in bulb-on state!

So that's all we need to know to hack this problem now. But how to get the amount of squares that are less than n, quite simple. Sqrt(n) is the answer, since all square numbers that is less than n will be 1, 4, 9 ... n and their corresponding square roots will be 1, 2, 3,... sqrt(n).

* Space cost O(1)
* Time cost O(1)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**&#x20;
* **Space Complexity:**&#x20;
