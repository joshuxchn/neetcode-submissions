# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root: return root
        #what defines a leaf node
            #if there is not a node to be added, then its a leaf node
            # or if the level is the same as leaf level, then

        #when do we need to check again
            #if there are no leaves at the bottom

        while True:
            q = deque()
            q.append((root, None, None))
            removed=False

            while q:
                node, parent, isitleft = q.popleft()
                if node.left: q.append((node.left, node, True))
                if node.right: q.append((node.right, node, False))

                if not node.left and not node.right: #leaf node
                    if node.val == target:
                        removed = True
                        if parent == None: return None #remove root
                        if isitleft: #was this the left child of the parent
                            parent.left = None
                        else: parent.right = None
                
            if not removed: return root

        return root
