# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Input: head = [3,2,0,-4], pos = 1
        Output: tail connects to node index 1
        """
        seen = set()

        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
 
        return None
        
