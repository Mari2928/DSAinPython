class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Input: nums = [-2,3,-2,4]
        Output: 48
        """
        maxPro = minPro = ans = nums[0]
        for num in nums[1:]:
            if num < 0:
                maxPro, minPro = minPro, maxPro
            maxPro = max(num, maxPro * num)
            minPro = min(num, minPro * num)
            if maxPro > ans:
                ans = maxPro
        return ans
        
