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

