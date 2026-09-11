# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {} 
        
        #max(rob, skip)
        def dfs(node, can_take):
            if not node: return 0
            if (node, can_take) in cache: return cache[(node, can_take)]

            skip = dfs(node.left, True) + dfs(node.right, True)
            take = 0
            if can_take:
                take = node.val + dfs(node.left, False) + dfs(node.right, False)
                

            cache[(node, can_take)] = max(take, skip)
            return cache[(node, can_take)]

        return dfs(root, True)

#skip skip skip skip take yadadada
#skip take skip skip take yadadada
    #need to cache yadada
    #needs to be 2d (account for if i took prior or not)