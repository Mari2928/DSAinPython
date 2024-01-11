class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        Input: n = 4, k = 2
        Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        """  
        result = []

        def backtrack(combination, next):
            if len(combination) == k:
                result.append(combination[:]) #[[1,2]]
                return
            
            for digit in range(next, n+1): # digit=1,2,3  next=2
                combination.append(digit)  # [1]-> [1,2]-> [1]-> [1,3]
                backtrack(combination, digit + 1) # ([1], 2)-> ([1,2], 3)
                combination.pop() # [1]
        
        backtrack([], 1)
        return result
        
