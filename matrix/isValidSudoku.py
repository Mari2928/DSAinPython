class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        result = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    # [8 . . . 8] -> (i, val) -> [(0, 8), (0, 8)] 
                    result += [(i, val), (val, j), (i // 3, j // 3, val)]
        return len(result) == len(set(result))
