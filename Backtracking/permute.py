class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        result = []
        
        def backtrack(combination, nums):
            if len(combination) == len(nums):
                result.append(combination[:]) #[[1,2,3]]
                return

            for num in nums: # 1-> 2-> 3
                if num not in combination:
                    combination.append(num) # [1,2] [1,3]   [2]   [3]
                    backtrack(combination, nums) # 1:[1,2,3],[1,3,2]  2:[2]  3:[3]
                    combination.pop() # [1]

        backtrack([], nums)
        return result
        

        
