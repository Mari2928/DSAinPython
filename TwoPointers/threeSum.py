class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]] -> (-1) + (-1) + 2 = 0
        """
        result = []
        n = len(nums)        
        nums.sort()

        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                triplet = nums[i] + nums[j] + nums[k] 
                if triplet > 0:
                    k -= 1
                elif triplet < 0:
                    j += 1
                else:    
                    ans =[nums[i], nums[j], nums[k]]    
                    if ans not in result:          
                        result.append(ans)
                    j += 1
                    k -= 1
        return result
