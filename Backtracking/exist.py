class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],word = "ABCCED"
        Output: true
        """
        seen = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, i, j, word, seen):
                    return True
        return False

    def backtrack(self, board, i, j, word, seen, pos=0):
        if pos == len(word):
            return True 
        
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 \
            or seen.get((i, j)) or word[pos] != board[i][j]:
            return False

        seen[(i, j)] = True
        result = self.backtrack(board, i+1, j, word, seen, pos + 1) \
                or self.backtrack(board, i-1, j, word, seen, pos + 1) \
                or self.backtrack(board, i, j+1, word, seen, pos + 1) \
                or self.backtrack(board, i, j-1, word, seen, pos + 1) 
        seen[(i, j)] = False

        return result          
