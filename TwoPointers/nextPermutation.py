class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Input: nums = [1,2,3]
        Output: [1,3,2]
        """
        for i in range(len(nums) - 2, -1, -1):    # i = 1
            for j in range(len(nums) - 1, i, -1): # j = 2
                if nums[i] < nums[j]:  # 2 < 3
                    nums[i], nums[j] = nums[j], nums[i] # [1,2,3] -> [1,3,2]
                    nums[i+1:] = nums[i+1:][::-1]   # [3] -> [3]
                    return
        nums.reverse() # [3,2,1] -> [1,2,3]
