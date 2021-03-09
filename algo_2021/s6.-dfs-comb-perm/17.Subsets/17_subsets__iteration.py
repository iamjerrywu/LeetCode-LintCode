class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = []

        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, subset, res):
        res.append(list(subset))
        print(res)
        
        for i in range(index, len(nums)):
            # [1] -> [1, 2]
            # go find all subsets that begin with [1, 2]
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, res)
            #[1, 2] => [1]
            subset.pop()
        
        
