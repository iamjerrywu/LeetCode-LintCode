# Two Sum III - Data Structure Design 607 \(E\)

## Problem

{% hint style="warning" %}
For this question, should ask which method would be called more often!
{% endhint %}

Design and implement a TwoSum class. It should support the following operations: `add` and `find`.

`add` - Add the number to an internal data structure.  
`find` - Find if there exists any pair of numbers which sum is equal to the value.Example

**Example 1:**

```text
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
```

## Solution - HashMap

Couldn't use hashset here, because we also want to record the occurrence time of each input

### Code

{% tabs %}
{% tab title="python" %}
```python
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.counter = {}
    
    def add(self, number):
        # write your code here
        self.counter[number] = self.counter.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        
        for num1 in self.counter:
            num2 = value - num1
            if num2 in self.counter:
                if num1 == num2 and self.counter[num1] < 2:
                    return False
                return True
                
        return False
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * AddNumber: O\(1\)
  * FindTwoSum: O\(n\)
* **Space Complexity: O\(n\)**
  * Create hashmap



## Solution - Two Pointer

Couldn't use hashset here, because we also want to record the occurrence time of each input

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * AddNumber: O\(n\)
  * FindTwoSum: O\(n\)
* **Space Complexity: O\(n\)**
  * Create array

