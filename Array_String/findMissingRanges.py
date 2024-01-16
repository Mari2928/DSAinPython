class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]

        Input: nums = [0,1,3,50,75], lower = 0, upper = 99
        Output: [[2,2],[4,49],[51,74],[76,99]]
        """
        result = []
        nums = [lower-1] + nums + [upper+1]

        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                result.append([nums[i-1]+1, nums[i]-1])
      
        return result
        
