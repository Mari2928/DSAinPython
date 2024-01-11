class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
        """
        result = []
        candidates.sort()
        
        def backtrack(combination, pos, target):
            if target == 0:
                result.append(combination[:])
                return

            for i in range(pos, len(candidates)):
                num = candidates[i]
                if target - num < 0:
                    return
                combination.append(num) # [2]-> [2,2]-> [2,2,2]-> [2,2,3]    
                backtrack(combination, i, target - num)
                combination.pop() # [2,2]
           
        backtrack([], 0, target)
        return result
        
