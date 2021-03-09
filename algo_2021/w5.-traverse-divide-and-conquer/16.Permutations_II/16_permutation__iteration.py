class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        # write your code here
        res = []
        if nums is None:
            return res

        if len(nums) == 0:
            res.append(list(res))
            return res
        
        nums.sort()
        self.dfs(nums, set(), [], res)
        return res
    
    def dfs(self, nums, visited, permutation, res):
        if len(permutation) == len(nums):
            res.append(list(permutation))
            return 
        
        for i in range(len(nums)):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                continue
            visited.add(i)
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, res)
            permutation.pop()
            visited.remove(i)