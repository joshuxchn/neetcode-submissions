# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = deque()
        qq = deque()
        if not p and not q: return True
        if p and not q or (not p and q): return False
        pq.append(p)
        qq.append(q)

        while qq and pq:
            q = qq.popleft()
            p = pq.popleft()
            if p.val != q.val: return False

            sameLeft = True
            if q.left: 
                qq.append(q.left)
                if not p.left: return False
            if p.left: 
                pq.append(p.left)
                if not q.left: return False

            if q.right: 
                qq.append(q.right)
                if not p.right: return False
            
            if p.right:
                pq.append(p.right)
                if not q.right: return False

            if len(pq) != len(qq): return False
        return True

