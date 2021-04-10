class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        for i in range(len(A)//2, -1, -1):
            self.down_shift(A, i)
    
    def down_shift(self, A, i):
        n = len(A)
        while i < n:
            left_id = i * 2 + 1
            right_id = i * 2 + 2 
            min_id = i
            if left_id < n and A[left_id] < A[min_id]:
                min_id = left_id
            if right_id < n and A[right_id] < A[min_id]:
                min_id = right_id
            
            if min_id == i:
                break

            A[i], A[min_id] = A[min_id], A[i]
            
            i = min_id