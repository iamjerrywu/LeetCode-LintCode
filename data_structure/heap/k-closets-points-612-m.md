# K Closets Points 612 \(M\)

## Problem

Given some `points` and an `origin` in two-dimensional space,Find `k` `points` from points which are closest to `origin` Euclidean.Return to the answer from small to large according to Euclidean distance. If two points have the same Euclidean distance, they are sorted by x values. If the x value is the same, then we sort it by the y value.Example

Example 1:

```text
Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3 
Output: [[1,1],[2,5],[4,4]]
```

Example 2:

```text
Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]
```

Challenge

O\(nlogn\) is OK, but can you think of a solution to O\(nlogk\)？

## Solution - Quick Select

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

* **Time Complexity: O\(n + klogk\)**
* **Space Complexity:**

## Solution - Max Heap

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
* **Space Complexity:**

\*\*\*\*

## Solution - Min Heap

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
* **Space Complexity:**

