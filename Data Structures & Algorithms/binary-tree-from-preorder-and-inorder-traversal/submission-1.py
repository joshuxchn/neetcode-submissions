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
            if l > r: #finished respective side
                return
            
            root_value = preorder[global_index]
            root = TreeNode(root_value)
            global_index += 1

            #find where the root exists in inorder (relative to its left and right)
            root_loc = LrootR[root_value]
            #we've found the split where mid exists. 
            #we know the left side has [0 to mid -1] nodes (similar for right)
                # so we recurse that amount of times
            root.left = dfs(l, root_loc - 1)
            root.right = dfs(root_loc + 1, r)

            return root
        
        return dfs(0, len(preorder)-1)

            