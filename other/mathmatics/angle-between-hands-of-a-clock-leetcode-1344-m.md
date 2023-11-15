# Angle Between Hands of a Clock (LeetCode 1344) (M)

## Problem



Given two numbers, `hour` and `minutes`, return _the smaller angle (in degrees) formed between the_ `hour` _and the_ `minute` _hand_.

Answers within `10-5` of the actual value will be accepted as correct.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/12/26/sample\_1\_1673.png)

```
Input: hour = 12, minutes = 30
Output: 165
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/12/26/sample\_2\_1673.png)

```
Input: hour = 3, minutes = 30
Output: 75
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/12/26/sample\_3\_1673.png)

```
Input: hour = 3, minutes = 15
Output: 7.5
```

&#x20;

**Constraints:**

* `1 <= hour <= 12`
* `0 <= minutes <= 59`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hr_angle = hour * 30 + 30 * (minutes/60)
        min_angle = 360 * (minutes/60)
        
        ans = abs(hr_angle - min_angle)
        return min(ans, 360 - ans)
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

* **Time Complexity: O(1)**
* **Space Complexity: O(1)**
