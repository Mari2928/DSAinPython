# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = 

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]
        """
        l1 = head
        l2 = head
        for _ in range(n):
            l2 = l2.next
        if not l2:  return head.next
        while l2.next:
            l1 = l1.next
            l2 = l2.next        
        l1.next = l1.next.next
        return head
        
