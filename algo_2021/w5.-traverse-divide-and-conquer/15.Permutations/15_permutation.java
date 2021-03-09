class Solution {
    /*
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public List<List<Integer>> permute(int[] nums) {
        // write your code here
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null) {
            return res;
        }

        if (nums.length == 0) {
            res.add(new ArrayList<Integer>());
            return res;
        }

        boolean[] visited = new boolean[nums.length];
        dfs(nums, visited, new ArrayList<Integer>(), res);
        return res;
    }

    private void dfs(int[] nums,
                     boolean[] visited, 
                     List<Integer> permutation,
                     List<List<Integer>> res
                    ) {
        if (permutation.size() == nums.length) {
            res.add(new ArrayList<Integer>(permutation));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            permutation.add(nums[i]);
            dfs(nums, visited, permutation, res);
            permutation.remove(permutation.size() - 1);
            visited[i] = false;
        }