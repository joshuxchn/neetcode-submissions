# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def bfs(root):
            if not root:
                return
            nonlocal res
            
            if root.val <= high and root.val >= low:
                res += root.val
                print(root.val, res)
                bfs(root.left)
                bfs(root.right)
            elif root.val < low:
                bfs(root.right)
            elif root.val > high:
                bfs(root.left)

        bfs(root)
        return res