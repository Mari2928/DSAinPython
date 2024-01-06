class Solution(object):
    def removeDuplicates(self, nums):
        """
        Remove the duplicates in-place.
        :type nums: List[int]
        :rtype: int
        
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        """
        nums[:] = sorted(set(nums))        
        return len(nums)

        
