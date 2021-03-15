DX = [0, 1, -1, 0]
DY = [1, 0, 0, -1]
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board:
            return []
        if board[0] is None or len(board[0]) == 0:
            return []
        visited = [[None] * len(board[0]) for _ in range(len(board))]
        prefix_is_word = self.get_prefix_set(words)
        # result should be set since there might be duplicate collected vocabularies
        res = set()
        # traverse all point inside board as start point 
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited[i][j] = True
                self.dfs(board, visited, i, j, board[i][j], prefix_is_word, res)
                visited[i][j] = False
        return list(res)
    
    def get_prefix_set(self, words):
        prefix_is_word = {}
        for word in words:
            for i in range(len(word)):
                prefix = word[:i + 1]
                # store all the prefix in dictionary and as False
                if prefix not in prefix_is_word:
                    prefix_is_word[prefix] = False
            # store all the word in dictionary as True, some might modify the prefix value
            prefix_is_word[word] = True
        return prefix_is_word
    
    def inside(self, board, x, y):
        return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])
    
    def dfs(self, board, visited, x, y, word, prefix_is_word, res):
        # pruning, if prefix not valid, then don't need to go further
        if word not in prefix_is_word:
            return
        
        if prefix_is_word[word]:
            res.add(word)
        
        for i in range(4):
            new_x = x + DX[i]
            new_y = y + DY[i]
            # WARNING!
            # first check boundary then check whether visited!
            if not self.inside(board, new_x, new_y) or visited[new_x][new_y]:
                continue
            
            visited[new_x][new_y] = True
            self.dfs(board, visited, new_x, new_y, word + board[new_x][new_y], prefix_is_word, res)
            visited[new_x][new_y] = False
        