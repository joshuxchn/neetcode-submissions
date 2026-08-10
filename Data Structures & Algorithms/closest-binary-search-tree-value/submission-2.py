# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        while root:
            curr_diff = abs(root.val - target)
            closest_diff = abs(closest - target)

            if curr_diff < closest_diff:    
                closest = root.val
            elif curr_diff == closest_diff:
                closest = min(closest, root.val)
            
            if target < root.val:
                root = root.left  # Target is smaller, go left
            else:
                root = root.right # Target is larger, go right
                
        return closest
                
