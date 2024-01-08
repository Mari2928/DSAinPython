class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]] 
        :rtype: int

        Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
        Output: 4
        """
        n = len(board)
        board.reverse()
        def label_to_pos(label):
            r = (label-1) // n
            c = (label-1) % n
            if r % 2:
                c = n - 1 - c
            return r, c
        Q = []
        Q.append([1, 0])
        seen = []
        while Q:
            label, step = Q.pop(0)
            for i in range(1, 7):            
                new_label = label + i
                r, c = label_to_pos(new_label)
                if board[r][c] != -1:
                    new_label = board[r][c]
                if new_label == n * n:
                    return step+1
                if new_label not in seen:
                    seen.append(new_label)
                    Q.append([new_label, step+1])
        return -1


        
