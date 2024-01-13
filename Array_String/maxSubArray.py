class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: sum([4,-1,2,1]) = 6
        """
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum, 0) + num
            if curSum > maxSum:
                maxSum = curSum
        return maxSum
