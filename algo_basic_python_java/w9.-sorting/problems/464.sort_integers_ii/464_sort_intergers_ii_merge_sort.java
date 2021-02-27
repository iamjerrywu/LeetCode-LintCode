public class Solution {
    /**
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers2(int[] A) {
        // write your code here
        int[] tmp = new int[A.length];
        mergeSort(A, 0, A.length - 1, tmp);
    }
    private void mergeSort(int[] A, int start, int end, int[] tmp) {
        // when split into single element, return
        if (start >= end) {
            return;
        }
        int mid = start + (end - start)/2; 
        // keep split in half
        mergeSort(A, start, mid, tmp);
        mergeSort(A, mid + 1, end, tmp);
        // merge two half array into tmp
        merge(A, start, end, tmp);
    }
    
    private void merge(int[] A, int start, int end, int[] tmp) {
        int n = end - start + 1;
        int mid = (start + end) / 2;
        int left = start, right = mid + 1;
        
        for (int k = 0; k < n; k++) {
            // merge two sorted arrays
            if ((left <= mid) && (right > end || A[left] <= A[right])) {
                tmp[k] = A[left];
                left++;
            } else {
                tmp[k] = A[right];
                right++;
            }
        }
        
        // assign back to original array A
        for (int k = 0; k < n; k++) {
            A[start + k] = tmp[k];
        }
    }
}