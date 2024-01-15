"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node

        Input: root = [1,2,3,4,5,null,7]
        Output: [1,#,2,3,#,4,5,7,#]
           1 -> None
          / \
         2 ->3 -> None
        """
        if not root:
            return root
            
        Q = [root]
        while Q:
            level = []
            for i in range(len(Q)):
                node = Q.pop(0)   
                level.append(node)             
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)                

            for i in range(1, len(level)):
                level[i-1].next = level[i]
        return root
        
