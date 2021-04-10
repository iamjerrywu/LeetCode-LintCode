class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        # WARNIN!
        # start + 1 < end, not start < end
        # To avoid if repeated target value, condition falling in dead lock 
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else: # nums[mid] == target:
                return mid
        
        # search again in start/end
        # since above while loop end when reaching two element left (start + end)
        # these two still need check up 
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1