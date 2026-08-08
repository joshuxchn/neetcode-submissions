# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        n = ""
        curr = head
        while curr:
            n = n + str(curr.val)
            curr = curr.next   
        
        n = int(n) + 1
        h = x = ListNode()
        for num in str(n):
            x.next = ListNode(int(num))
            x = x.next
        
        return h.next
