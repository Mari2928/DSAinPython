class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.

        Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        """
        zeroToOne = []
        oneToZero = []
        row = len(board)
        col = len(board[0])

        def isOne(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == 0:
                return 0
            else: 
                return 1

        for i in range(row):
            for j in range(col):
                numOnes = 0
                numOnes += isOne(i+1, j) + isOne(i-1, j) + isOne(i, j+1) + isOne(i, j-1)\
                         + isOne(i-1, j-1) + isOne(i-1, j+1) + isOne(i+1, j-1) + isOne(i+1, j+1)
                if board[i][j] == 1 and (numOnes < 2 or numOnes > 3):
                    oneToZero.append((i, j))
                elif board[i][j] == 0 and numOnes == 3:
                    zeroToOne.append((i, j))

        for i, j in oneToZero:
            board[i][j] = 0
        
        for i, j in zeroToOne:
            board[i][j] = 1

        
