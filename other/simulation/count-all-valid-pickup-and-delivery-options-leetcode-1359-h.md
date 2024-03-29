# Count All Valid Pickup and Delivery Options (LeetCode 1359) (H)



## Problem

&#x20;

Given `n` orders, each order consist in pickup and delivery services.&#x20;

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).&#x20;

Since the answer may be too large, return it modulo 10^9 + 7.

&#x20;

**Example 1:**

```
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
```

**Example 2:**

```
Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
```

**Example 3:**

```
Input: n = 3
Output: 90
```

&#x20;

**Constraints:**

* `1 <= n <= 500`

## Solution

![](<../../.gitbook/assets/Screen Shot 2021-10-17 at 9.20.23 PM.png>)



{% tabs %}
{% tab title="Python" %}
```python
MOD = 10 ** 9 + 7
class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range(1, n + 1):
            res*=(1 + (2*i - 1))/2 * (2 * i - 1)
            res%=MOD
        return int(res)
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
