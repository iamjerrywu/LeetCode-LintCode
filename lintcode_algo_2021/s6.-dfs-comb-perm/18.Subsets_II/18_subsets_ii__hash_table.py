class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        res = []
        visited = {}
        nums.sort()
        self.dfs(nums, 0, [], res, visited)
        return res
    def get_hash(self, subset):
        hash_string = ""
        for item in subset:
            hash_string += str(item)
            hash_string += "_"
        return hash_string
        
    def dfs(self, nums, index, subset, res, visited):
        hash_string = self.get_hash(subset)
        if hash_string in visited:
            return 
        visited[hash_string] = True
        res.append(list(subset))
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, res, visited)
            subset.pop()