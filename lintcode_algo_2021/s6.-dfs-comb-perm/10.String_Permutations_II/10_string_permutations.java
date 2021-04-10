public class Solution {
    /**
     * @param str: A string
     * @return: all permutations
     */
    public List<String> stringPermutation2(String str) {
        // write your code here
        List<String> res = new ArrayList<>();
        
        if (str == null) {
            return res;
        }
        char[] s = str.toCharArray();
        // sort array 
        Arrays.sort(s);
        dfs(0, s, new boolean[str.length()], "", res);
        return res;
    }

    private void dfs(int index, 
                     char[] s, 
                     boolean[] visited, 
                     String permutation,
                     List<String> res) {
        if (permutation.length() == s.length) {    
            res.add(permutation);
            return;
        }
        for (int i = 0; i < s.length; i++) {
            if (visited[i] == true) {
                continue;
            }
            if (i > 0 && s[i] == s[i - 1] && visited[i - 1] == false) {
                continue;
            }            
            visited[i] = true;
            // WARNING!
            // Here since at the same level we don't want to keep to s[i] in String
            // Pass it to call stack frame instead of adding in the same loop level
            dfs(i, s, visited, permutation + s[i], res);
            visited[i] = false;
        }
    }
}