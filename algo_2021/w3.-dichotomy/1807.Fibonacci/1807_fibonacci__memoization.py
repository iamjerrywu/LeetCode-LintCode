class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        return self.memoize(n)
        
    def memoize(self, n):
        # init memory
        cache = {1:0, 2:1}
        for i in range(3, n + 1):
            # implement memory 
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]