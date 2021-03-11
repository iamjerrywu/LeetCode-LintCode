public class Solution {
    /*
     * @param A: Given an integer array
     * @return: nothing
     */
    public void heapify(int[] A) {
        // write your code here
        for (int i = 0; i < A.length; i++) {
            shiftUp(A, i);
        }
    }
    private void shiftUp(int[] A, int i) {
        while (i != 0) {
            int father = (i - 1)/2;
            if (A[i] > A[father]) {
                break;
            }
            int tmp = A[i];
            A[i] = A[father];
            A[father] = tmp;

            i = father;
        }
    }
}