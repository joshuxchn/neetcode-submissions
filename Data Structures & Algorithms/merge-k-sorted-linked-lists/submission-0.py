# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        #dummy
        #insert remove functions

        curr = dummyHead = ListNode()
        nums = []
        for linked in lists:
            while linked:
                nums.append(linked.val)
                linked = linked.next
        nums.sort()

        for n in nums:
            curr.next = ListNode(n)
            curr = curr.next

        return dummyHead.next