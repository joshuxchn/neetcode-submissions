# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l2 = self.reverse_list(l2)
        l1 = self.reverse_list(l1)

        head = l1
        carry = 0
        prev = None
        while l1 or l2:
            val = carry
            if l2:
                val += l2.val
                l2 = l2.next
            if l1:
                val += l1.val  
            else: #no l1 but yes l2
                prev.next = ListNode()
                l1 = prev.next #update l1
            
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0

            l1.val = val  
            prev = l1    
            l1 = l1.next
        
        if carry == 1:
            print("asdfasdf")
            prev.next = ListNode(1, None)

        head = self.reverse_list(head)
        return head
    

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        return prev