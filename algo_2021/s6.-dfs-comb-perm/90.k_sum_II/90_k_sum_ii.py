class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        A = sorted(A)
        res = []
        self.dfs(0, A, k, target, [], res)
        return res
    def dfs(self, index, A, k, target, subset, res):
        if k == 0 and target == 0:
            res.append(list(subset))
            return 
        # pruning 
        if k == 0 or target < 0:
            return 
        for i in range(index, len(A)):
            subset.append(A[i])
            # need to i + 1, since don't want to pick the same number 
            self.dfs(i + 1, A, k - 1, target - A[i], subset, res)
            subset.pop()