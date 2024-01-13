class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Input: nums = [1,1,2]
        Output:
        [[1,1,2],
         [1,2,1],
         [2,1,1]]
        """
        result = []
        n = len(nums)
        seen = [False] * n

        def backtrack(comb):
            if len(comb) == n:
                if comb not in result:
                    result.append(comb[:])
                return

            for i in range(n):
                if seen[i]:
                    continue
                comb.append(nums[i])
                seen[i] = True
                backtrack(comb)
                seen[i] = False
                comb.pop()

        backtrack([])
        return result
