# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            return Node(insertVal)

        found = False
        prev = head
        curr = head.next

        while True:
            #edge case, insert at front (ex: 10, 9, 3 : insert 4)
            prev = curr
            curr = curr.next
            
            #case 1: prev < val < curr
            if prev.val < insertVal and curr.val >= insertVal:
                found = True
                break

            #case 2: prev > curr (end of order), and val > prev (needs to go after prev)
            if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                found = True
                break

            if prev == head or found:
                break
                
        new_node = Node(insertVal, curr)
        prev.next = new_node


        return head