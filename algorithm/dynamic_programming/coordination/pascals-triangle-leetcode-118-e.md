# Pascal's Triangle (LeetCode 118) (E)

## Problem



Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

&#x20;

**Example 1:**

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Example 2:**

```
Input: numRows = 1
Output: [[1]]
```

&#x20;

**Constraints:**

* `1 <= numRows <= 30`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * numRows for _ in range(numRows)]
        
        idx = 0
        # init 
        for i in range(numRows):
            dp[i][0] = 1
            dp[i][idx] = 1
            idx+=1
        
        if numRows < 3:
            return self.build_ans(dp)
        
        length = 2
        for i in range(2, numRows):
            for j in range(1, length):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            length+=1
        return self.build_ans(dp)
    
    def build_ans(self, dp):
        ans = []
        tmp = []
        for lst in dp:
            for num in lst:
                if num == 0:
                    ans.append(tmp)
                    tmp = []
                    break
                tmp.append(num)
            if tmp:
                ans.append(tmp)
        return ans
        
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

* **Time Complexity:**
* **Space Complexity:**

