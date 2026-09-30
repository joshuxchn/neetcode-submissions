# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def dfs(node, curr_sum):
            nonlocal best

            if not node:
                return 0

            # Either continue the path from above,
            # or restart the path at this node.
            curr_sum = max(
                curr_sum + node.val,
                node.val
            )

            # Best downward paths starting from each child.
            # Ignore them if they're negative.
            left = max(0, dfs(node.left, curr_sum))
            right = max(0, dfs(node.right, curr_sum))

            # Continue the path from above through ONE branch.
            add = curr_sum + max(left, right)

            # Current node is the turning point:
            # left -> node -> right
            start = node.val + left + right

            best = max(best, curr_sum, add, start)

            # What we give our parent:
            # parent can only extend through one branch.
            return node.val + max(left, right)

        dfs(root, 0)
        return best