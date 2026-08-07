# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        l = 1
        test = head
        while test.next:
            l += 1
            test = test.next
        k = k % l
        if k == 0:
            return head
        
        curr = head
        while curr.next and l-k-1 != 0:
            curr = curr.next
            k += 1

        t = curr.next
        curr.next = None
        test.next = head
        head = t

        return head

        