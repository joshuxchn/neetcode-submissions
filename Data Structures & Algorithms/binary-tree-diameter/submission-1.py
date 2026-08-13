# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            #diamater at this node, compared to the best diamater
            res = max(res, left + right)
                #this is the left, right heights starting from this node
                #the recursive calls backtrack up, so the parent will have
                    #1 + our result
        
            return 1 + max(left, right)
        
        dfs(root)
        return res