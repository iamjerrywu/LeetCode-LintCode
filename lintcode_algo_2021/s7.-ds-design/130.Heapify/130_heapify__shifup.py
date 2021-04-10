class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A)):
            self.shift_up(A, i)
    
    def shift_up(self, A, i):
        while i != 0:
            father = (i - 1) // 2
            if A[i] > A[father]:
                break
            A[i], A[father] = A[father], A[i]
            i = father
        