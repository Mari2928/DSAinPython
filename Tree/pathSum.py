class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Input: nums = [113,215,221]
        Output: 12
           3
          / \
         5   1
        """
        tree = {(x // 100, x // 10 % 10) : x % 10 for x in nums}
        
        def dfs(depth, pos, sum):
            if (depth, pos) not in tree:
                return 0

            left = (depth + 1, pos * 2 - 1) # (2, 1) -> (3, 3)
            right = (depth + 1, pos * 2)    # (2, 2) -> (3, 4)
            val = tree[(depth, pos)]        # 3 -> 1

            if left not in tree and right not in tree:
                return sum + val # 3 + 1

            # dfs(2, 1, 3) + dfs(2, 2, 3) = 0 + 4
            return dfs(left[0], left[1], sum + val) \ 
                    + dfs(right[0], right[1], sum + val)

        return dfs(1, 1, 0)
