# Jump Game VII 5765 \(M\)

## Problem



You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

* `i + minJump <= j <= min(i + maxJump, s.length - 1)`, and
* `s[j] == '0'`.

Return `true` if you can reach index `s.length - 1` in `s`_, or_ `false` _otherwise._

**Example 1:**

```text
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
```

**Example 2:**

```text
Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
```

**Constraints:**

* `2 <= s.length <= 105`
* `s[i]` is either `'0'` or `'1'`.
* `s[0] == '0'`
* `1 <= minJump <= maxJump < s.length`

## Solution - DFS with Memoization

{% hint style="danger" %}
Since n.length reach 10^5, DFS even with memoization would still LTE or exceed stack maximum depth
{% endhint %}

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        return self.dfs(0, s, minJump, maxJump, set())
    
    def dfs(self, index, s, minJump, maxJump, visited):
        if index < len(s):
            if s[index] == '1':
                return
            if index == len(s) - 1:
                return True
            if index in visited:
                return 
            visited.add(index)
        else:
            return 
        for inc in range(minJump, maxJump + 1):
            if self.dfs(index + inc, s, minJump, maxJump, visited):
                return True
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        return self.dfs(0, s, minJump, maxJump, set())
    
    def dfs(self, index, s, minJump, maxJump, visited):
        if index < len(s):
            if s[index] == '1':
                return
            if index == len(s) - 1:
                return True
            if index in visited:
                return 
            visited.add(index)
        else:
            return 
        for inc in range(minJump, maxJump + 1):
            if self.dfs(index + inc, s, minJump, maxJump, visited):
                return True
        return False
```

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False
        
        n = len(s)
        dp = [False] * n
        
        dp[0] = True
        
        for i in range(1, n):
            if i - maxJump < 0:
                start = 0
            else:
                start = max(i - maxJump, 0)
            for j in range(start, i - minJump + 1):
                if dp[j] == True and s[i] == '0':
                    dp[i] = True
        return dp[n - 1]
                
```

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False
        
        n = len(s)
        dp = [False] * n
        dp[0] = True
        cnt = 1
        
        for i in range(minJump, n):
            if cnt and s[i] == '0':
                dp[i] = True
            cnt+=dp[i + 1 - minJump] - dp[i - maxJump] * (i >= maxJump)
            
        return dp[n - 1]
                
```

