# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        tally = 0
        #think of it as:
        #if Node x is greater than all the values up to the root
        def dfs(node, minVal):
            nonlocal tally
            if not node: return
            if node.val >= minVal: 
                tally += 1
                minVal = node.val
            dfs(node.left, minVal)
            dfs(node.right, minVal)
        dfs(root, -101)
        return tally