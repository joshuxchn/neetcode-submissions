# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(
        self,
        root: Optional[TreeNode],
        key: int
    ) -> Optional[TreeNode]:

        def find(node):
            """
            Iteratively find:
            1. The node containing key
            2. That node's parent

            Returns (None, parent) if key does not exist.
            """
            parent = None

            while node and node.val != key:
                parent = node

                if key < node.val:
                    node = node.left
                else:
                    node = node.right

            return node, parent

        # Locate the node that should be deleted.
        node, parent = find(root)

        #no children: replacement becomes none
        replacement = None
        if not node: #nothing to replace
            return root

        if not node.left:
            replacement = node.right
        elif not node.right:
            replacement = node.left
        

        else:
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor =successor.left

            if successor_parent is not node:
                #the right remaining tree off the leftmost section
                successor_parent.left = successor.right

                #connect deleted node's right tree back to successor
                successor.right = node.right
            
            successor.left = node.left
            replacement = successor

        if parent is None:
            return replacement #root node case
        else:
            #which side of parent
            if parent.left is node:
                parent.left = replacement
            else:
                parent.right = replacement
        return root

