class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        Input: candidates = [10,1,2,7,6,1,5], target = 8
        Output: 
        [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
        ]
        """
        result = []
        candidates.sort()

        def backtrack(combination, pos, target):
            if target == 0:
                if combination not in result:
                    result.append(combination[:])
                return            

            prev = None
            for i in range(pos, len(candidates)):
                num = candidates[i]
                if target - num < 0:
                    return
                if prev == num:
                    continue
                prev = num
                combination.append(num)
                backtrack(combination, i+1, target - num)
                combination.pop()

        backtrack([], 0, target)
        return result
