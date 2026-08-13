# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #greater than a, less than b
        def valid(node, a, b):
            if not node:
                return True
            
            if not (a < node.val < b):
                return False
            return valid(node.left, a, node.val) and valid(node.right, node.val, b)


        return valid(root, -1000000000, 1000000000)