# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return root
        if p.val > q.val: p,q=q,p

        def lca(node):
            print(node.val)
            if node.val < p.val:
                return lca(node.right)
            elif node.val > q.val:
                return lca(node.left)
            else:
                return node

        return lca(root)
