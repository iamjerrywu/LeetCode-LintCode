public class Solution {
    /**
     * @param M: a matrix
     * @return: the total number of friend circles among all the students
     */
    public int findCircleNum(int[][] M) {
        // Write your code here
        Queue<Integer> queue = new LinkedList<Integer>();
        boolean[] visited = new boolean[M.length];
        int cnt = 0;

        for (int roll = 0; roll < M.length; roll++) {
            if (visited[roll] == true) 
                continue;
            queue.offer(roll);
            while (!queue.isEmpty()) {
                int poll = queue.poll();
                for (int col = 0; col < M[poll].length; col++) {
                    if ((M[poll][col] != 1) || (visited[col] == true)) 
                        continue;
                    queue.offer(col);
                    visited[col] = true;
                }
            }
            cnt++;
        }
        return cnt;
    }
}