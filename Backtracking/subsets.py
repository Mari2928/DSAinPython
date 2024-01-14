class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        """
        result = []

        def backtrack(nums, subset):
            result.append(subset)
            for i in range(len(nums)):
                backtrack(nums[i+1:], subset + [nums[i]])

        backtrack(nums, [])
        return result        
