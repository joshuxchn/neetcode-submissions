# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            p, q = q, p
        def helper(node):
            if not node:
                return
            print(node.val)
            
            if node.val == p.val or node.val == q.val:
                print("asdf", node.val)
                return node

            #case 2: if splits, then its ancestor
            if q.val > node.val and p.val < node.val:
                return node

            if p.val > node.val:
                return helper(node.right)
            elif q.val < node.val:
                return helper(node.left)
            
            
        return helper(root)