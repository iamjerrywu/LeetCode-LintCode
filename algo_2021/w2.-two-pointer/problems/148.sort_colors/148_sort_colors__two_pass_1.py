class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        if not nums:
        return 
        
        # init cnts array 
        cnts = [0 for _ in range(3)]
        for num in nums:
           cnts[num]+= 1
        
        k = 0
        # traverse cnts array and assign new value to nums 
        for i in range(len(cnts)):
            cnt = cnts[i]
            while cnt:
                nums[k] = i
                cnt-=1
                k+=1
        return nums  