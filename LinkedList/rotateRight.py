# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        Input: head = [1,2,3,4,5], k = 2
        Output: [4,5,1,2,3
        """
        if not head:
            return None
            
        length = 1
        node = head

        while node.next:
            node = node.next
            length += 1
        k = k % length

        # make SLL circle
        node.next = head

        # rotate
        for _ in range(length - k - 1):
            head = head.next

        # keep answer and cut the circle
        ans = head.next
        head.next = None

        return ans
        
