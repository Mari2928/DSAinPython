# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]] 

        Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
        Output: [[5,4,11,2],[5,8,4,5]] (root-to-leaf paths)
        """
        result = []
        def dfs(root, path):
            if root is None:
                return
            if not root.left and not root.right:
                path.append(root.val)
                if sum(path) == targetSum:
                    result.append(path[:])
                return 

            path.append(root.val)
            dfs(root.left, path[:])
            dfs(root.right, path[:])

        dfs(root, [])
        return result
            
        
