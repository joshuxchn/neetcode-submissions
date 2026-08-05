# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = two = ""
        while l1:
            one = str(l1.val) + one
            l1 = l1.next
        while l2:
            two = str(l2.val) + two
            l2 = l2.next
        l = []
        s = int(one) + int(two)
        for c in str(s):
            l.append(c)
        
        head = h = ListNode()
        for n in reversed(l):
            head.next = ListNode(n)
            head = head.next

        return h.next