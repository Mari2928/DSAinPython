# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode

        Input: head = [1,4,3,2,5,2], x = 3
        Output: [1,2,2,4,3,5]
        """
        node = head
        beforeStart = None
        beforeEnd = None
        afterStart = None
        afterEnd = None
      
        while node:
            next = node.next
            node.next = None # trim from original to avoid cycle
            if node.val < x:
                if not beforeStart:
                    beforeStart = node
                    beforeEnd = beforeStart
                else:
                    beforeEnd.next = node
                    beforeEnd = node    # move forward
            else:
                if not afterStart:
                    afterStart = node
                    afterEnd = afterStart
                else:
                    afterEnd.next = node
                    afterEnd = node
            node = next

        if not beforeStart: 
            return afterStart

        beforeEnd.next = afterStart
        return beforeStart 
            
