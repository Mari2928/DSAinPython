from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str

        Input: nums = [3,30,34,5,9]
        Output: "9534330"
        """       
        nums = [str(num) for num in nums]
        
        def compare(n, m):
            if n + m > m + n:
                return -1
            else:
                return 1
                
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))
