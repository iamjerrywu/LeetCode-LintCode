# Legal Number Statistics II 1659 \(E\)

## Problem

Given `n` integers and m queries, each query containing two integers `L`, `R`, for each quey output how many integers are in the range between `[L, R]`.Example

**Example 1**

```text
Input: a=[1,2,3,4,5,6],q=[[1,2],[1,5]]
Output: [2,5]
Explanation:
For query[1,2], there are a[0],a[1] are legal.
For query[1,5], there are a[0],a[1],a[2],a[3],a[4] are legal
```

**Example 2**

```text
Input : a=[1,5,3,3,3,2],q=[[1,2]]
Output: [2]
Explanation:
For query[1,2], only a[0],a[5] are legal.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param a: the array a
    @param q: the queries q
    @return: for each query, return the number of legal integers 
    """
    def getAns(self, a, q):
        # write your code here
        res = []
        if not a or not q:
            return res
        for i in range(len(q)):
            cnt = 0
            for item in a:
                if q[i][0] <= item <= q[i][1]:
                    cnt+=1
            res.append(cnt)
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

