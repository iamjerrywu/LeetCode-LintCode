public class Solution {
    /**
     * @param A: an integer array
     * @param k: a postive integer <= length(A)
     * @param targer: an integer
     * @return: A list of lists of integer
     */
    public List<List<Integer>> kSumII(int[] A, int k, int target) {
        // write your code here
        Arrays.sort(A);
        List<List<Integer>> res = new ArrayList<>();
        dfs(0, A, k, target, new ArrayList<Integer>(), res);
        return res;
    }
    private void dfs(int index, 
                     int[] A, 
                     int k, 
                     int target, 
                     ArrayList<Integer> subset, 
                     List<List<Integer>> res) {
        if (k == 0 && target == 0) {
            res.add(new ArrayList<Integer>(subset));
            return;
        }
        // pruning
        if (k == 0 || target < 0) {
            return;
        }
        for (int i = index; i < A.length; i++) {
            subset.add(A[i]);
            dfs(i + 1, A, k - 1, target - A[i], subset, res);
            subset.remove(subset.size() - 1);
        }
    }
}