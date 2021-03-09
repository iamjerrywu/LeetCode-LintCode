class Result:
    def __init__(self):
        self.min_cost = float('inf')
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        # Write your code here
        graph = self.construct_graph(roads, n)
        res = Result()
        self.dfs(1, n, set([1]), 0, graph, res)
        return res.min_cost
    
    def dfs(self, city, n, visited, cost, graph, res):
        # once traversed all the cities, update the result
        if len(visited) == n:
            res.min_cost = min(res.min_cost, cost)  
            return
        
        # traverse all the city's route
        for next_city in graph[city]:
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(next_city, n, visited, cost + graph[city][next_city], graph, res)
            visited.remove(next_city)          
    
    def construct_graph(self, roads, n):
        graph = {
            i : {j : float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for city_1, city_2, cost in roads:
            # since there might be several different cost btw two cities
            # should pick the minimum one
            graph[city_1][city_2] = min(graph[city_1][city_2], cost)
            graph[city_2][city_1] = min(graph[city_2][city_1], cost)
        return graph