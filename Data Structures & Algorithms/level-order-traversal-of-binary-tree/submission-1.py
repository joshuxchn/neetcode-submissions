# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = deque()
        if not root:
            return []
        q.append(root)

        while q:
            nodes = []
            values = []
            while q:
                nodes.append(q[0])
                values.append(q.popleft().val)
            result.append(values)

            for node in nodes:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return result