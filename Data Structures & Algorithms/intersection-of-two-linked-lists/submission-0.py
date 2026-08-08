# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB
        loop_againA = True
        loop_againB = True
        while currA and currB:
            if currA == currB:
                return currA

            currA = currA.next
            currB = currB.next

            if not currA and loop_againA:
                loop_againA = False
                currA = headB
            if not currB and loop_againB:
                loop_againB = False
                currB = headA

        return None
