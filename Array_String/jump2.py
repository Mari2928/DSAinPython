class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Input: nums = [2,3,1,1,4]
        Output: 2
        """
        stepsLeft = 0
        jumps = 0
        position = 0

        for i in range(len(nums) - 1): # 4: 0 -> 1 -> 2
            stepsLeft = max(stepsLeft, i + nums[i]) # (0,0+2) -> (2,1+3)-> (4,2+1)
            if i == position:
                jumps += 1 # 1 -> 2
                position = stepsLeft # 2 -> 4
        return jumps
        
        
