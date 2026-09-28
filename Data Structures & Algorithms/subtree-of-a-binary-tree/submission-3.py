# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        r_inorder = []
        s_inorder = []
        #python passes (everything) list as reference
        def inorder(node, l):
            if not node: 
                return l.append(None)
                

            inorder(node.left, l)
            
            inorder(node.right, l)
            l.append(node.val)
        inorder(r, r_inorder)
        inorder(s, s_inorder)
        
        n = len(s_inorder)
        print(r_inorder, s_inorder)
        for i in range(len(r_inorder)-n+1):
            if r_inorder[i:i+n] == s_inorder: return True
        return False




            
