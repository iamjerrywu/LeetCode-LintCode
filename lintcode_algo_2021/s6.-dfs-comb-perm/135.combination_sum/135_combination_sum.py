class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        res = []
        if str is None:
            return res     
        str = sorted(str)
        self.dfs(0, str, set(), [], res)
        return res
        
    def dfs(self, index, str, visited, permutation, res):
        if len(visited) == len(str):
            # output as string 
            res.append(''.join(permutation))
            return
        for i in range(len(str)):
            if i in visited:
                continue
            # eliminate the repeated values 
            if i > 0 and str[i] == str[i - 1] and i - 1 not in visited:
                continue
            visited.add(i)
            permutation.append(str[i])
            self.dfs(i, str, visited, permutation, res)
            permutation.pop()
            visited.remove(i)
