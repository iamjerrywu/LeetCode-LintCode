class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        ref = {}
        for i in range(len(numbers)):
            if target - numbers[i] in ref:
                return [ref[target - numbers[i]], i]
            ref[numbers[i]] = i
        return [-1, -1]