class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        return self.divide_conquer(triangle, 0, 0)
    
    def divide_conquer(self, triangle, x, y):
        if x == len(triangle):
            return 0
        left = self.divide_conquer(triangle, x + 1, y)
        right = self.divide_conquer(triangle, x + 1, y + 1)
        return min(left, right) + triangle[x][y]
