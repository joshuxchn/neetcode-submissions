# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        prev = None

        while slow:
            t = slow.next
            slow.next = prev

            prev = slow
            slow = t
        
        curr = head
        h2 = prev

        while curr:
            print(curr.val, h2.val)
            if curr.val != h2.val:
                return False
            h2 = h2.next
            curr = curr.next


        return True
