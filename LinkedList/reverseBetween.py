class Solution:
    def reverseBetween(self, head, left, right):
        """
        Input: head = [1,2,3,4,5], left = 2, right = 4 # <- index
        Output: [1,4,3,2,5]
        """
        if left == right:
            return head
        
        dummyNode = ListNode(0)
        dummyNode.next = head
        prev = dummyNode

        for _ in range(left - 1):
            prev = prev.next
        
        # reverse the [left, right] nodes
        cur = prev.next
        reverse = None
        for _ in range(right - left + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        prev.next.next = cur
        prev.next = reverse
        
        return dummyNode.next
