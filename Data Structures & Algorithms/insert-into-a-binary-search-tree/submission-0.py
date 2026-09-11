# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if not root: return newNode

        node = root
        prev = None
        while node:
            prev = node
            if val > node.val:
                node = node.right
            else:
                node = node.left
            print(prev.val)
        if val > prev.val:
            prev.right = newNode
        else:
            prev.left = newNode

        return root