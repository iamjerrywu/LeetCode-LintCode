# Final Discounted Price

## Problem

A shopkeeper needs to complete a sales task. He arranges the items for sale in a row.  
Starting from the left, the shopkeeper subtracts the price of the first lower or the same price item on the right side of the item from its full price.  
If there is no item to the right that costs less than or equal to the current item's price, the current item is sold at full price.  
You should return the actual selling price of each item.

* The length of Prices is within range: \[1, 100000\]
* Prices\[i\] is within range: \[1, 1000000\]

Example

**Example 1:**

```text
Input:Prices = [2, 3, 1, 2, 4, 2]Output: [1, 2, 1, 0, 2, 2]Explanation: The item 0 and 1 are each discounted by 1 unit, The item 3 at 2 units, is discounted 2 units, as would the item 4 at 4 units. 
```

**Example 2:**

```text
Input:Prices = [1, 2, 3, 4, 5]Output:[1, 2, 3, 4, 5]Explanation: each item should keep full price beacause there are not equal or lower priced items to the right
```

## Solution - Brute Force \(Simulation\)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param prices: a list of integer
    @return: return the actual prices
    """
    def FinalDiscountedPrice(self, prices):
        # write your code here
        res = list(prices)
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
  * n: len\(prices\)
* **Space Complexity: O\(n\)**

## Solution - Monotone Stack

In this case, we maintain a monotone stack that the value inside should always be ascending



### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param prices: a list of integer
    @return: return the actual prices
    """
    def FinalDiscountedPrice(self, prices):
        # write your code here
        stack = []
        res = list(prices)

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop()
            stack.append(i)
        
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(2n\) = O\(n\)**
  * n: len\(prices\)
  * Every element is visited twice
* **Space Complexity: O\(n\)**

