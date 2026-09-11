# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        
        #reverse helper
        #dummy, 1, 3, 4
        def reverse(node, prev):
            for i in range(k):
                temp = node.next
                node.next=prev

                prev=node
                if i != k-1: node=temp
            return node #ends at k node
        
        #dummy head
        dummy = ListNode()
        dummy.next = head
        slow = head
        fast = dummy

        #turtle rabbit skip ahead, if not k nodes return
        must_break=False
        def iterate():
            nonlocal fast, must_break
            for i in range(k):
                if not fast.next:
                    must_break = True
                    break
                fast = fast.next
            return fast.next


        iterate()
        #nodes start and end of sector
        start = slow
        end = None
        #nodes prior and after sector
        prior = dummy
        after = fast.next

        while True:
            if must_break: return dummy.next
            
            end = reverse(start, prior)
            start.next = after
            prior.next = end
            
            
            prior = start
            fast = prior
            start = after
            after = iterate()

        return dummy.next


        


        
        
