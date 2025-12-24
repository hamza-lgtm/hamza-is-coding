# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        def dfs(node):
            if not node:
                return ""
            if not node.right and not node.left:
                return str(node.val) 
            elif not node.right:
                return str(node.val) + '('+  dfs(node.left) +')'
            return str(node.val) + '('+  dfs(node.left) +')'+'('+ dfs(node.right)+')'
            



        return dfs(root)
