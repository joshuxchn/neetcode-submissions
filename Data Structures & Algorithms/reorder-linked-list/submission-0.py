# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.find_mid(head)
        l2 = self.reverse_list(mid.next)
        mid.next = None

        first = head
        second = l2
        while second:
            #a->b, x->y
            t1 = first.next
            t2 = second.next

            first.next = second
            #a -> x -> y

            second.next = t1
            #a -> x -> b

            first = t1
            #first = b

            second = t2
            #second = y
        
        #(next iteration) a->x->b
        #a-> x -> b->y
        #a -> x -> b -> y -> None
        #b = None, y = None
        

    def find_mid(self, head):
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev

            prev = head
            head = temp
        return prev
            
