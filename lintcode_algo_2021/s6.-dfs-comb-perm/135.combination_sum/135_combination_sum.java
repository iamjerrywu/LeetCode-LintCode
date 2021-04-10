public class Solution {
    /**
     * @param candidates: A list of integers
     * @param target: An integer
     * @return: A list of lists of integers
     */
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // write your code here

        List<List<Integer>> res = new ArrayList<>();
        if (candidates.length == 0) {
            return res;
        }
        candidates = removeDuplicates(candidates);
        dfs(0, target, candidates, new ArrayList<Integer>(), res);
        return res;
    }

    private int[] removeDuplicates(int[] candidates) {
        Arrays.sort(candidates);
        int index = 0;
        for (int i = 0; i < candidates.length; i++) {
            // remove duplicate ones 
            if (candidates[i] != candidates[index]) {
                index++;
                candidates[index] = candidates[i];
            }
        }

        int[] candidatesNew = new int[index + 1];
        for (int i = 0; i < index + 1; i++) {
            candidatesNew[i] = candidates[i];
        }
        return candidatesNew;
    }

    private void dfs(int index, 
                     int target, 
                     int[] candidates, 
                     List<Integer> combination, 
                     List<List<Integer>> res) {
        if (target == 0) {
            // deep copy
            res.add(new ArrayList<Integer>(combination));
            return;
        }
        if (target < 0) {
            return;
        }
        for (int i = index; i < candidates.length; i++) {
            combination.add(candidates[i]);
            dfs(i, target - candidates[i], candidates, combination, res);
            combination.remove(combination.size() - 1);
        }
    }
}