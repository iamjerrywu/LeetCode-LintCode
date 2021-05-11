# Gas Station 187 \(M\)

## Problem

There are _N_ gas stations along a circular route, where the amount of gas at station _i_ is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station i to its next station \(_i_+1\). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

The solution is guaranteed to be unique.Example

**Example 1:**

```text
Input:gas[i]=[1,1,3,1],cost[i]=[2,2,1,1]
Output:2
```

**Example 2:**

```text
Input:gas[i]=[1,1,3,1],cost[i]=[2,2,10,1]
Output:-1
```

Challenge

O\(n\) time and O\(1\) extra space

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if sum(gas) < sum(cost):
            return -1
        
        index = 0
        remained_gas = 0
        for i in range(len(gas)):
            remained_gas+=gas[i] - cost[i]
            if remained_gas < 0:
                remained_gas = 0
                index = i + 1
        return index
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

