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
        #WARNING
        # has to be deep copy, since list pass by reference
        res.append(list(subset))
        
        for i in range(index, len(nums)):
            # [1] -> [1, 2]
            # go find all subsets that begin with [1, 2]
            
            # ignore repeated values
            # since the repeated values would be same level, and it must appeard after index
            # moreover, i should not ==0, since i - 1 would out of bound
            if i != 0 and nums[i] == nums[i - 1] and i > index:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, res)
            #[1, 2] => [1]
            subset.pop()
        
        
