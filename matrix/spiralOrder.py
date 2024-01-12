class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [1,2,3,6,9,8,7,4,5]
        """
        result = []
      
        # peel from the outer layer
        while matrix and matrix[0]:
            print('iteration')
            if matrix[0]:
                result += matrix.pop(0)
                print('1', result)

            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
                print('2', result)   

            if matrix and matrix[-1]:
                result += matrix.pop()[::-1]
                print('3', result)

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
                print('4', result)

        return result

    """
    iteration
    ('1', [1, 2, 3])
    ('2', [1, 2, 3, 6, 9])
    ('3', [1, 2, 3, 6, 9, 8, 7])
    ('4', [1, 2, 3, 6, 9, 8, 7, 4])
    iteration
    ('1', [1, 2, 3, 6, 9, 8, 7, 4, 5])

    """
        
