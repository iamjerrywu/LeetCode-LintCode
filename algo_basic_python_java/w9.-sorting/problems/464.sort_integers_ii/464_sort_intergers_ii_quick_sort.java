public class Solution {
    /**
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers2(int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            return;
        }
        // start quick sort 
        quickSort(A, 0, A.length - 1);
    }

    private void quickSort(int[] A, int start, int end) {
        if (start >= end) {
            return;
        }
     
        int left = start, right = end;

        // 1. select pivot, between A[start], A[end], get value not index 
        int pivot = A[start + (end - start)/2];

        // 2. left <= right not left < right
        while (left <= right) {
            // traverse left and right for values that need to be swap
            while(left <= right && A[left] < pivot) {
                left++;
            }
            while(left <= right && A[right] > pivot) {
                right--;
            }
            // swap value 
            if (left <= right) {
                int tmp = A[left];
                A[left] = A[right];
                A[right] = tmp;
                left++;
                right--;
            }
        }
        // keep sorting the rmained left/right parts
        quickSort(A, start, right);
        quickSort(A, left, end);
    }
}