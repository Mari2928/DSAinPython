class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Input: nums = [3,2,1,2,1,7]
        Output: 6 ->  [3,4,1,2,5,7]
        """
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                change = nums[i-1] - nums[i] + 1
                nums[i] += change
                count += change
        return count
        
