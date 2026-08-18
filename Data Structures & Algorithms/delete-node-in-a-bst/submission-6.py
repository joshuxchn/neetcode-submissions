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

        # The key does not exist, so nothing changes.
        if not node:
            return root

        # ---------------------------------------------------------
        # Decide which node/subtree will replace the deleted node.
        # ---------------------------------------------------------

        # Case 1: No left child.
        #
        # This handles:
        # - No children: replacement becomes None
        # - Only a right child: replacement becomes node.right
        replacement = None
        if not node.left:
            replacement = node.right

        # Case 2: Only a left child.
        elif not node.right:
            replacement = node.left

        # Case 3: Two children.
        else:
            # Find the in-order successor:
            # the smallest node in the right subtree.
            successor_parent = node
            successor = node.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            # If the successor is deeper than node.right,
            # remove it from its original position.
            #
            # The successor cannot have a left child, but it may
            # have a right child, so preserve that right subtree.
            if successor_parent is not node:
                successor_parent.left = successor.right

                # Move the deleted node's right subtree underneath
                # the successor.
                successor.right = node.right

            # Move the deleted node's left subtree underneath
            # the successor.
            successor.left = node.left

            replacement = successor

        # ---------------------------------------------------------
        # Connect the deleted node's parent to its replacement.
        # ---------------------------------------------------------

        # If parent is None, we are deleting the root.
        if parent is None:
            return replacement

        # Otherwise, determine which side of the parent held node.
        if parent.left is node:
            parent.left = replacement
        else:
            parent.right = replacement

        return root