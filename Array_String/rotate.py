class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        """
        if not nums or not k:
            return None
        
        k %= len(nums)
        if k:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
