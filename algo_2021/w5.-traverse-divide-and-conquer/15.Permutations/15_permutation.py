class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        if nums == None: 
            return res
        if len(nums) == 0:
            res.append(list(res))
            return res
        self.dfs(0, nums, set(), [], res)
        return res
    
    def dfs(self, index, nums, visited, permutation, res):
        if len(visited) == len(nums):
            # WARNING!
            # should deep copy list since list is pass by reference 
            res.append(list(permutation))
            return
        for i in range(len(nums)):
            if i in visited:
                continue
            # add to already visited 
            visited.add(i)
            permutation.append(nums[i])
            self.dfs(i, nums, visited, permutation, res)
            # backtracing, remove top element
            permutation.pop()
            # remove already visited record
            visited.remove(i)
