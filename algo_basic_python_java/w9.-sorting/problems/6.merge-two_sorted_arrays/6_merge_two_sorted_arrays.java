public class Solution {
    /**
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        // write your code here
        int a = 0, b = 0;
        // pointers to A, B respeactively
        int la = A.length, lb = B.length;
        int[] res = new int[la + lb];

        for (int k = 0; k < la + lb; k++) {
            // WARNING!
            // b should >= lb, since when equals the index is already out of range
            if (a < la && (b >=lb || A[a] < B[b])) {
                res[k] = A[a];
                a++;
            } else {
                res[k] = B[b];
                b++;
            }
        }
        return res;
    }
}
Complexity Analysis