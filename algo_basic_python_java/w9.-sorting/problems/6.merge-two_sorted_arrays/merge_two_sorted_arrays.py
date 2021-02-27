class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        la, lb = len(A), len(B)
        # pointers to A, B respeactively
        a, b = 0, 0
        res = [0] * (la + lb)
        
        for k in range(la + lb):
            # WARNING!
            # b should >= lb, since when equals the index is already out of range
            if a < la and (b >= lb or A[a] < B[b]):
                res[k] = A[a]
                a+=1
            else:
                res[k] = B[b]
                b+=1
        return res