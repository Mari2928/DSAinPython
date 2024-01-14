class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        """
        n = len(nums) - 1
        i = j = 0
        
        while j <= n:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            else: 
                j += 1
        
