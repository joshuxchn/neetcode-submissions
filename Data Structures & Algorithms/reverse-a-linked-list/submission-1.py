# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        #prev -> a -> b -> c
        while curr:
            temp = curr.next 
            #temp = b
            #temp = c
            #temp = None

            curr.next = prev
            #a->prev
            #b -> a
            #c -> b -> a


            prev = curr
            # a (prev) -> None,
            # b (prev) -> a -> None
            # c (prev) -> b -> a -> None

            curr = temp
            # b (curr) -> c
            # c (curr)
            # curr = None

        #b -> a, c
        #c -> b -> a
        return prev