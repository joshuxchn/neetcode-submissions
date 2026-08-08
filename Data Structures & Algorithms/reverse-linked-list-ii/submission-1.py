# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = r = head
        prev = None
        #adjust pointers
        for i in range(left - 1):
            prev = l
            l = l.next
        for i in range(right - 1):
            r = r.next
        #store head for later, and the one after R to reconnect pointers
        if left == 1: head = r
        after = r.next
        original_l = l
        #store stop point
        s = r.next

        #reversal
        p = None
        while l != s:
            self.print_list(head)

            t = l.next
            l.next = p

            p = l
            l = t
    
        #reconnect ends
        original_l.next = s
        if prev:
            prev.next = r
        
        return head


    def print_list(self, head):
        # Start at the head node
        current = head
        
        # Loop until the end of the list (where current is None)
        while current:
            print(current.val, end=" -> ")
            current = current.next  # Move to the next node
            
        print("None")  # Visual indicator for the end of the list