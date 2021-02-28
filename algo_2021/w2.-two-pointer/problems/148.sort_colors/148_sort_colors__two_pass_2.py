class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    
    def sortColors(self, nums):
        # 3 elements require 2 partition 
        self.partition(nums, 1)
        self.partition(nums, 2)
    def partition(self, nums, k):
        last_small_pointer = -1
        for cur in range(len(nums)):
            if nums[cur] < k:
                last_small_pointer+=1
                # swap value
                nums[last_small_pointer], nums[cur] = nums[cur], nums[last_small_pointer]