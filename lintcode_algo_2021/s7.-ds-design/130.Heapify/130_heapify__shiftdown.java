public class Solution {
    /*
     * @param A: Given an integer array
     * @return: nothing
     */
    public void heapify(int[] A) {
        // write your code here
        for (int i = (A.length - 2)/2; i >= 0; i--) {
            shiftDown(A, i);
        }
    }

    private void shiftDown(int[] A, int index) {
        int n = A.length;
        while (index < n) {
            int right = index * 2 + 1;
            int left = index * 2 + 2;
            int minIndex = index;

            if (left < n && A[left] < A[minIndex]) {
                minIndex = left;
            }

            if (right < n && A[right] < A[minIndex]) {
                minIndex = right;
            }

            if (index == minIndex) {
                break;
            }

            int tmp = A[minIndex];
            A[minIndex] = A[index];
            A[index] = tmp;

            index = minIndex;
        }
    }
}