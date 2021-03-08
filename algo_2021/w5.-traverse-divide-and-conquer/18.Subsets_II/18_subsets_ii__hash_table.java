public class Solution {
    /**
     * @param nums: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        HashMap<String, Boolean> visited = new HashMap<String, Boolean>();
        Arrays.sort(nums);
        dfs(nums, 0, new ArrayList<>(), subsets, visited);
        
        return subsets;
    }
    
    String getHash(List<Integer> subset) {
        String hashString = "";
        for (int i = 0;i < subset.size(); i++) {
            hashString += subset.get(i).toString();
            hashString += "_";
        }
        return hashString;
    }
    
    void dfs(int[] nums, 
             int startIndex, 
             List<Integer> subset,
             List<List<Integer>> subsets,
             HashMap<String, Boolean> visited) {
        String hashString = getHash(subset);
        
        if (visited.containsKey(hashString)) {
            return ;
        }
        
        visited.put(hashString, true);
        subsets.add(new ArrayList<Integer>(subset));
        for (int i = startIndex;i < nums.length; i++) {
            subset.add(nums[i]);
            dfs(nums, i + 1, subset, subsets, visited);
            subset.remove(subset.size() - 1);
        } 
    } 
}