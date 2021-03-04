public class Solution {
    /**
     * @param A: an array
     * @return: total of reverse pairs
     */
    public long reversePairs(int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            return 0;
        }
        
        int[] tmp = new int[A.length];
        return mergeSort(A, 0, A.length - 1, tmp);

    }

    private int mergeSort(int[] A, int start, int end, int[] tmp) {
        
        if (start >= end) {
            return 0;
        }
        int cnt = 0;
        int mid = start + (end - start)/2;

        cnt += mergeSort(A, start, mid, tmp);
        cnt += mergeSort(A, mid + 1, end, tmp);
        cnt += merge(A, start, end, tmp);

        return cnt;
    }

    private int merge(int [] A, int start, int end, int[] tmp) {
        int n = end - start + 1;
        int mid = start + (end - start)/2;
        int left = start, right = mid + 1;
        int cnt = 0;

        for (int k = 0; k < n; k++) {
            if ((left <= mid) && (right > end || A[left] <= A[right])) {
                tmp[k] = A[left];
                left++;
            } else {
                tmp[k] = A[right];
                right++;
                if(left <= mid) {
                   cnt += (mid - left + 1); 
                }
            }
        }

        for (int k = 0; k < n; k++) {
            A[start + k] = tmp[k];
        }

        return cnt;
    }
}