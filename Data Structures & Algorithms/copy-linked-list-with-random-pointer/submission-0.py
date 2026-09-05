"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #no duplicate nodes - have a hashmap of old to new
        #cyclical edge case
        old_to_new = {}

        if not head: return None

        curr = head
        newHead = None
        
        while curr:
            #create copy node
            if curr in old_to_new: copy = old_to_new[curr]
            else:
                copy = Node(curr.val)
                old_to_new[curr] = copy

            #attatch 
            if not curr.next: old_to_new[curr.next] = None
            elif curr.next not in old_to_new:
                old_to_new[curr.next] = Node(curr.next.val)

            copy.next = old_to_new[curr.next]

            #attatch random
            if not curr.random: old_to_new[curr.random] = None #null case
            elif curr.random not in old_to_new:
                old_to_new[curr.random] = Node(curr.random.val)

            copy.random = old_to_new[curr.random]           

            if not newHead: newHead = copy
            curr = curr.next


        return newHead