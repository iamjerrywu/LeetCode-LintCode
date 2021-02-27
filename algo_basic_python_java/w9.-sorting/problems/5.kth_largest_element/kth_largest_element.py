class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums:
            return -1
        return self.quick_select(nums, 0, len(nums) - 1, n)
    
    def quick_select(self, nums, start, end, n):
        if start == end:
            return nums[start]
        
        left = start
        right = end
        pivot = nums[start + (end - start)//2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left+=1
            while left <= right and nums[right] < pivot:
                right-=1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        
        #WARNING!
        # if k = 1th, then start == j, also k start from 1
        if start + n - 1 <= right:
            return self.quick_select(nums, start, right, n)
        if start + n - 1 >= left:
            #WARNING!
            # since left part don't care, k should reduct them
            return self.quick_select(nums, left, end, n - (left - start ))
        return nums[right + 1]