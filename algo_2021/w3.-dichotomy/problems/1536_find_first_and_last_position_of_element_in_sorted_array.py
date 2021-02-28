class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        # write your code here
        if not nums:
            return -1
        res = []
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                # first position so end as mid
                end = mid
        
        if nums[start] == target:
            res.append(start)
        elif nums[end] == target:
            res.append(end)

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                # last position so start as mid
                start = mid
        
        if nums[end] == target:
            res.append(end)
        elif nums[start] == target:
            res.append(start)
        
        if not res:
            return [-1, -1]
        return res