# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Input: root = [3,9,20,null,null,15,7]
        Output: 3
        """
        if root == None: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
