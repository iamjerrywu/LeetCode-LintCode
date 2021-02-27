class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A: 
            return
        
        tmp = [0 for _ in range(len(A))]
        self.merge_sort(A, 0, len(A) - 1, tmp)
    
    def merge_sort(self, A, start, end, tmp):
        # when split into single element, return 
        if start >= end:
            return 
        mid = start + (end - start)//2
        # keep split in half
        self.merge_sort(A, start, mid, tmp)
        self.merge_sort(A, mid + 1, end, tmp)
        # merge the two half array into tmp
        self.merge(A, start, end, tmp)
    
    def merge(self, A, start, end, tmp):
        left = start
        mid = start + (end - start)//2
        right = mid + 1
        n = end - start + 1
        
        for k in range(n):
            # merge two sorted arrays
            if left <= mid and (right > end or A[left] <= A[right]):
                tmp[k] = A[left]
                left+=1
            else:
                tmp[k] = A[right]
                right+=1
        # assign back to original array A
        for k in range(n):
            A[start + k] = tmp[k]
        

        
   