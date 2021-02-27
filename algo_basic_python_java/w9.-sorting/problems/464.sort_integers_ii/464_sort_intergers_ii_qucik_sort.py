class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A: 
            return 
        self.quick_sort_helper(A, 0, len(A) - 1)
    def quick_sort_helper(self, A, start, end):
        if start >= end:
            return 
        
        left, right = start, end
        # select pivot 
        pivot = A[start + (end - start)//2]
        
        while left <= right:
            # shift left if value < pivot
            while left <= right and A[left] < pivot:
                left+=1
            
            # shift right if value > pivot
            while right >= left and A[right] > pivot:
                right-=1
            
            # exchange value
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left+=1
                right-=1
        
        # keep doing partition        
        self.quick_sort_helper(A, start, right)
        self.quick_sort_helper(A, left, end)