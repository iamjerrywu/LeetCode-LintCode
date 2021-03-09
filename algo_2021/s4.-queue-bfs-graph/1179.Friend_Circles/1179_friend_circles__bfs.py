class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        queue = collections.deque()
        visited = [False] * len(M)
        cnt = 0
        
        # BFS, search by level
        # start traverse roll 
        for roll in range(len(M)):
            # if row already searched, skip
            if visited[roll]:
                continue
            queue.append(roll)
            # if queue not empty, means still have connection within this group
            while queue:
                poll = queue.popleft()
                # start traverse in column
                for col in range(len(M[poll])):
                    # if that column value is not 1, or already visited, skip
                    if M[poll][col] != 1 or visited[col]:
                        continue
                    queue.append(col)
                    visited[col] = True
            # after entire while loop, mean this group's all connections have been searched
            cnt+=1
        return cnt        