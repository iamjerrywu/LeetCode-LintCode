# Lake Escape 1828 \(H\)

## Problem

Albert is stranded on a frozen lake. He is currently on a snowbank that gives him some traction. but once he steps the ice, he will slide in the same direction until he hits another snowbank. There are also treacherous holes in the ice that he must avoid.

As a cruel twist of fate, Albert's young pup, Kuna, is also stranded, but on a different snowbank. Can Albert reach his pup AND make it to shore?

Albert can only move horizontally and vertically. He makes it to shore by leaving the lake grid.

The input contains these parameters:

* side\_length: the length of a side of the lake \(it's a square\)
* lake\_grid: a 2D matrix representing the lake 0 = ice, 1 = snowbank, -1 = hole
* albert\_row: row of Alber'ts snowbank
* albert\_column: column of Albert's snowbank
* kuna\_row: row of Kuna's snowbank
* kuna\_column: column of Kuna's snowbank

It is guaranteed \|albert\\_row-kuna\\_row\|+\|albert\\_column- kuna\\_column\|&gt;0∣albert\_row−kuna\_row∣+∣albert\_column−kuna\_column∣&gt;0。Example

**Example 1:**

```text
Input:7[[0,0,0,0,0,0,0],[0,0,-1,0,0,0,0],[0,0,1,-1,0,-1,0],[-1,0,1,0,0,0,0],[0,1,1,0,0,1,0],[-1,0,-1,0,-1,0,0],[0,0,0,0,0,0,0]]4132Output: trueExplanation:As it seen in the picture. Yellow ceil is Albert's location and red ceil is Kuna's location. Albert can turn right to (4,2) and up to (3,2) then turn right to leave the lake grid.
```

![&#x56FE;&#x7247;](https://media.jiuzhang.com/media/markdown/images/2/20/c06db360-53ec-11ea-ab9e-0242c0a8d005.jpg)

Challenge

Albert can't go to the shore and then find Kuna.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

