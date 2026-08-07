# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        #calibrate fast
        l = 0
        test = head
        while test:
            l += 1
            test = test.next
        if l == 0:
            return head
        k = k % l

        while fast and k != 0:
            fast = fast.next
            k -= 1
        
        while fast and fast.next: #calibrate pointers, stop 1 before none
            slow = slow.next
            fast = fast.next
        
        if fast == slow:
            return head

        temp = slow.next
        slow.next = None
        fast.next = head
        head = temp

        return head

        