# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        #prev, a -> b -> c
        while curr:
            #temp = b
            temp = curr.next 

            #a->prev, b -> c
            curr.next = prev

            #b -> a, c
            prev = curr
            curr = temp

        return prev