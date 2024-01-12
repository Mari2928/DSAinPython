class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        """
        row = set()
        col = set()

        # record positions of 0s
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        # flip to 0s
        for i in row:
            for j in range(len(matrix[0])):
               matrix[i][j] = 0
        
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j] = 0
