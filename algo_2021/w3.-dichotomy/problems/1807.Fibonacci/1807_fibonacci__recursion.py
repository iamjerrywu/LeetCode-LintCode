class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        return self.fibonacci(n - 2) + self.fibonacci(n - 1)