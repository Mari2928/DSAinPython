class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Input: nums = [1,2,1,3,5,6,4]
        Output: 5
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            if start == end:
                return start
            mid = (start + end) / 2
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid       

        return mid    
