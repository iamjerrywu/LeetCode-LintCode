class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        return self.binary_search(nums, 0, len(nums) - 1, target)
    
    def binary_search(self, nums, start, end, target):
        
        # if cannot find values, eventually reach here
        # WARNING!
        # not start >= end, since even when one element, still need to find out
        if start > end: 
            return -1
        
        mid = start + (end - start)//2
        # find which parts the target will locate 
        if nums[mid] == target:
            return mid
        # if target > mid value, means it's possibly and only in the right side
        if nums[mid] < target:
            return self.binary_search(nums, mid + 1, end, target)
        # if target < mid value, means it's possibly and only in the left side
        return self.binary_search(nums, start, mid - 1, target)