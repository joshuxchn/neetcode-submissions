# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node, local_max):
            nonlocal count
            if not node:
                return
            
            if node.val >= local_max:
                count += 1

                local_max = node.val
            dfs(node.left, local_max)
            dfs(node.right, local_max)
        
        dfs(root, -101)
        return count