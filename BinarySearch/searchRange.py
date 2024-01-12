class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
        """
        if not nums:
            return [-1, -1]

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                start = end = mid 
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1
                return [start+1, end-1]

            if target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
        
