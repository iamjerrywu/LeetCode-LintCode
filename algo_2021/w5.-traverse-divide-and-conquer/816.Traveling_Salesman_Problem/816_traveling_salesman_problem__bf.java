class Result {
    int minCost;
    public Result() {
        minCost = Integer.MAX_VALUE;
    }
}

public class Solution {
    /**
     * @param n: an integer,denote the number of cities
     * @param roads: a list of three-tuples,denote the road between cities
     * @return: return the minimum cost to travel all cities
     */
    public int minCost(int n, int[][] roads) {
        // Write your code here
        int[][]graph = constructGraph(roads, n);
        Set<Integer> visited = new HashSet<>();
        Result res = new Result();
        visited.add(1);
        dfs(1, n, visited, 0, graph, res);
        return res.minCost;
    }

    private void dfs(int city,
                     int n, 
                     Set<Integer> visited,
                     int cost,
                     int[][] graph,
                     Result res) {
        if (visited.size() == n) {
            res.minCost = Math.min(res.minCost, cost);
            return;
        }
        
     // Here would traverse all the route
        for ( int i = 1; i < graph[city].length; i++) {
            if (visited.contains(i)) {
                continue;
            }
            visited.add(i);
            dfs(i, n, visited, cost + graph[city][i], graph, res);
            visited.remove(i);
        }
    }

    int[][] constructGraph(int[][] roads, int n) {
        int[][] graph = new int[n + 1][n + 1];
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < n + 1; j++) {
                // since later would calculate the total sum
                // those default value (MAX_VALUE) would be added as well
                // to avoid overflow, right shift 4 bits
                graph[i][j] = Integer.MAX_VALUE >> 4;
            }
        }
        for (int i = 0; i < roads.length; i++) {
            int city1 = roads[i][0];
            int city2 = roads[i][1];
            int cost = roads[i][2];
            graph[city1][city2] = Math.min(graph[city1][city2], cost);
            graph[city2][city1] = Math.min(graph[city2][city1], cost);
        }

        return graph;
    }
}