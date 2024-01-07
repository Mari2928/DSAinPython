# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7
        """
        if root is None: return root
        Q = []
        Q.append(root)
        res = []
        while Q:
            level = []
            for i in range(len(Q)):
                node = Q.pop(0)
                level.append(node.val)
                if node.left is not None: Q.append(node.left)
                if node.right is not None: Q.append(node.right)
            res.append(level)
        return res

        
