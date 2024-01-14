# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Input: root = [2,1,3]
        Output: true

        Input: root = [5,1,4,null,null,3,6]
        Output: false
        """
        def check(root, maxVal, minVal):
            if root == None:
                return True
            if root.val >= maxVal or root.val <= minVal:
                return False

            return check(root.left, root.val, minVal) and check(root.right, maxVal, root.val)

        return check(root, float('inf'), float('-inf'))
        
