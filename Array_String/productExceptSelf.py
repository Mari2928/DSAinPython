class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        """
        result = []
        temp = 1
        for num in nums:        # [1,2,3,4]
            result.append(temp) # [1,1,2,6]
            temp *= num

        temp = 1
        for i in reversed(range(len(nums))):
            result[i] *= temp   # [24,12,8,6]
            temp *= nums[i]
        return result

        
        
        

        
