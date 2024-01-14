class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Input: nums = [1,2,2]
        Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        """
        result = []
        nums.sort()

        def backtrack(nums, subset):
            if subset not in result:
                result.append(subset)
            for i in range(len(nums)):
                backtrack(nums[i+1:], subset + [nums[i]])

        backtrack(nums, [])
        return result        
