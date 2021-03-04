class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        
        nums = [(number, index) for index, number in enumerate(numbers)]
        
        # nlogn
        nums.sort()
        
        # n
        left = 0
        right = len(nums) - 1
        while left < right:
            # change the pointer position depend on its relationship with target
            if nums[left][0] + nums[right][0] > target:
                right-=1
            elif nums[left][0] + nums[right][0] < target:
                left+=1
            else:
                return sorted([nums[left][1], nums[right][1]])
        return[-1, -1]