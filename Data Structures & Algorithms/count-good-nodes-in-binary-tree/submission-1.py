# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        if not root: return 0

        def dfs(node, localmax):
            nonlocal total
            if not node: return
            if node.val >= localmax: 
                total += 1
                localmax = node.val
            dfs(node.left, localmax)
            dfs(node.right, localmax)
        
        dfs(root, root.val)

        return total