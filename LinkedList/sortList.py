# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Input: head = [-1,5,3,4,0]
        Output: [-1,0,3,4,5]
        """
        if not head:
            return head

        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next

        nodes = sorted(nodes)
        node = ListNode(nodes[0])
        head = node
        for i in range(1, len(nodes)):
            node.next = ListNode(nodes[i])
            node = node.next
        
        return head
        
