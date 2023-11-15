# Sell Diminishing-Valued Colored Balls (LeetCode 1648) (M)

## Problem



You have an `inventory` of different colored balls, and there is a customer that wants `orders` balls of **any** color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls **of that color** you currently have in your `inventory`. For example, if you own `6` yellow balls, the customer would pay `6` for the first yellow ball. After the transaction, there are only `5` yellow balls left, so the next yellow ball is then valued at `5` (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, `inventory`, where `inventory[i]` represents the number of balls of the `ith` color that you initially own. You are also given an integer `orders`, which represents the total number of balls that the customer wants. You can sell the balls **in any order**.

Return _the **maximum** total value that you can attain after selling_ `orders` _colored balls_. As the answer may be too large, return it **modulo** `109 + 7`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/jj.gif)

```
Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
```

**Example 2:**

```
Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
```

&#x20;

**Constraints:**

* `1 <= inventory.length <= 105`
* `1 <= inventory[i] <= 109`
* `1 <= orders <= min(sum(inventory[i]), 109)`



## Solution - Heap (TLE)

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
    int maxProfit(vector<int>& inventory, int orders) {
        priority_queue<int> pq;
        
        for (int val : inventory) {
            pq.push(val);
        }
        
        int res = 0;
        
        while (!pq.empty()) {
            if (orders == 0) return res;
            int val =pq.top();
            pq.pop();
            if (val > 1) pq.push((val - 1));
            res+=val;
            res%=modulo;
            orders-=1;
        }
        return res;
    }
private:
    const long modulo = 10e9 + 7;
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n \* m)**
  * n: inventory length
  * m: inventory value&#x20;
* **Space Complexity:**

## Solution - Sort

![](<../../.gitbook/assets/Screen Shot 2022-01-15 at 5.48.51 PM.png>)

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
    int maxProfit(vector<int>& inventory, int orders) {
        sort(inventory.begin(), inventory.end(), compare);
        
        long k = 1;
        long res = 0;
        inventory.push_back(0);
        
        for (int i = 0; i < inventory.size() - 1; i++) {
            if (inventory[i] > inventory[i + 1]) {
                if (k * (inventory[i] - inventory[i + 1]) < orders) {
                    long diff = inventory[i] - inventory[i + 1];
                    res += k * (inventory[i] + inventory[i + 1] + 1) * (diff) / 2;
                    orders -=diff * k;
                    res %= modulo;
                } else {
                    long q = orders/k;
                    long r = orders%k;
                    res+= k * (inventory[i] + (inventory[i] - q + 1)) * (q - 1 + 1) / 2;
                    res+= r * (inventory[i] - q);
                    return res%modulo;
                }
            }
            k+=1;
        }
        return res;
    }
private:
    const long modulo = 1e9 + 7;
    
    static bool compare(int a, int b) {
        return a > b;
    }
};nfdd
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(nlogn)**
  * **n: inventory length**
* **Space Complexity:**



