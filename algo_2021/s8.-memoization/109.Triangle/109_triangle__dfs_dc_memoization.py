class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        return self.divide_conquer(triangle, 0, 0, {})
    
    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
        
        # memoization for pruning
        # avoid searching on the same node twice
        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        # first store in to dictionary
        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]
