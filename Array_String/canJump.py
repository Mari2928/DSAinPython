class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Input: nums = [2,3,1,1,4]
        Output: true
        """
        stepsLeft = nums[0]

        if not stepsLeft and len(nums) > 1:
            return False

        for num in nums[1:-1]: # 0 stepsLeft at last position holds, e.g.,[2,0,0]
            stepsLeft = max(stepsLeft - 1, num) 
            if not stepsLeft:
                return False
        return True
