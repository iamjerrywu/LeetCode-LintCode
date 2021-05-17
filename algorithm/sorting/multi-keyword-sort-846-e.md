# Multi-keyword Sort 846 \(E\)

## Problem

Given `n` students and their test scores, expressed as \(student number, test scores\), sort by test scores in descending order, if the test scores are the same, sort the student number in ascending order.Example

**Example1**

```text
Input: array = [[2,50],[1,50],[3,100]]
Output: [[3,100],[1,50],[2,50]]
```

**Example2**

```text
Input: array = [[2,50],[1,50],[3,50]]
Output: [[1,50],[2,50],[3,50]]
```

## 

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        # Write your code here
        if array == None:
            return array

        for i in range(len(array)):
            front = i
            for j in range(i, len(array)):
                if array[front][1] < array[j][1]:
                    front = j
                if array[front][1] == array[j][1] and array[front][0] > array[j][0]:
                    front = j
            array[i], array[front] = array[front], array[i]
        return array

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        # Write your code here
        array.sort(key = lambda  n : (-n[1], n[0]))
        return array
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

