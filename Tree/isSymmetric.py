# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Input: root = [1,2,2,3,4,4,3]
        Output: true
        """
        def check(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and check(node1.left, node2.right) \
                        and check(node1.right, node2.left)
            return node1 == node2

        return check(root.left, root.right)        
