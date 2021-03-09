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
        if index == len(nums):
            # WARNING!
            # Need to allocate new list
            # If not, would modify the same list since list is pass by reference
            res.append(list(subset))
            return
        
        # select nums[index]
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, res)
        
        # remove nums[index]
        subset.pop()
        self.dfs(nums, index + 1, subset, res)
        
