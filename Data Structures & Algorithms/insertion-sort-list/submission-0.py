# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            temp = curr.next

            if curr == head:
                curr.next = None
                curr = temp
                continue
            
            inner = head
            if curr.val <= inner.val:
                curr.next = inner
                head = curr
            else:
                prev = None
                while inner and curr.val > inner.val:
                    prev = inner
                    inner = inner.next
                prev.next = curr
                curr.next = inner

            curr = temp
        return head