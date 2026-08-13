# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        LrootR = {}
        for i in range(len(inorder)):
            LrootR[inorder[i]] = i
        
        global_index = 0
        def dfs(l, r):
            nonlocal global_index
            if l > r:
                return None

            #iterate through each preorder index, create node
            root_val = preorder[global_index]
            root = TreeNode(root_val)
            
            #find root in inorder array
            mid = LrootR[root_val]
            global_index += 1


            # recurse / add the left and right side
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

            
        return dfs(0, len(inorder) - 1)
            