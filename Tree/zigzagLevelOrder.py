# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[20,9],[15,7]]
        """
        if root is None: 
            return root

        result = []
        Q = [root]
        leftToRight = 1

        while Q:
            level = []
            for i in range(len(Q)):
                node = Q.pop(0)
                level.append(node.val)                
                if node.left: Q.append(node.left)
                if node.right: Q.append(node.right)
            
            if leftToRight == -1:
                level.reverse()
            leftToRight *= -1
            result.append(level)

        return result           
        
