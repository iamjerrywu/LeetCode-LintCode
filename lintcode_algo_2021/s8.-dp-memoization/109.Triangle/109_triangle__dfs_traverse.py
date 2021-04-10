class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        self.minimum = float('inf')
        self.traverse(triangle, 0, 0, 0)
        return self.minimum
    
    def traverse(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.minimum = min(path_sum, self.minimum)
            return 
        self.traverse(triangle, x + 1, y, path_sum + triangle[x][y])
        self.traverse(triangle, x + 1, y + 1, path_sum + triangle[x][y])
