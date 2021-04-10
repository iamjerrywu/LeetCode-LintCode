class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        
        pre_2, pre_1, cur = 0, 1, 1
        
        for i in range(3, n + 1):
            cur = pre_2 + pre_1
            pre_2 = pre_1
            pre_1 = cur
        return cur