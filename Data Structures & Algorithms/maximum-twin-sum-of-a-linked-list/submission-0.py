# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev

            prev = second
            second = temp
        second_head = prev
        res = 0
        print("break")
        while head:
            res = max(res, second_head.val + head.val)
            print(second_head.val, head.val)
            second_head = second_head.next
            head = head.next
        
        return res

