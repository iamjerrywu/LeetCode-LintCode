class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        # write your code here
        if not A:
            return 0
        tmp = [0 for _ in range(len(A))]
        return self.merge_sort(A, 0, len(A) - 1, tmp)
    
    def merge_sort(self, A, start, end, tmp):
        if start >= end: 
            return 0
        mid = start + (end - start)//2
        # record reversed paris num
        cnt = 0
        # left and right parts merge
        cnt += self.merge_sort(A, start, mid, tmp)
        cnt += self.merge_sort(A, mid + 1, end, tmp)

        # merge two sorted arrays
        cnt += self.merge(A, start, end, tmp)
        return cnt
    
    def merge(self, A, start, end, tmp):
        mid = start + (end - start)//2
        left, right = start, mid + 1
        n = end - start + 1
        
        #record reversed paris num
        cnt = 0
        for k in range(n):
            if left <= mid and (right > end or A[left] <= A[right]):
                tmp[k] = A[left]
                left+=1
            else:
                tmp[k] = A[right]
                right+=1
                if left <= mid:
                    cnt += mid - left + 1
        
        for k in range(n):
            A[start + k] = tmp[k]
        return cnt