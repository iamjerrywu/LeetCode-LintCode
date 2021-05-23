# Untitled

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        return self.dfs(0, s, minJump, maxJump)
    
    def dfs(self, index, s, minJump, maxJump):
        if index < len(s):
            if s[index] == '1':
                return
            if index == len(s) - 1:
                return True
        else:
            return 
        for inc in range(minJump, maxJump + 1):
            if self.dfs(index + inc, s, minJump, maxJump):
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

