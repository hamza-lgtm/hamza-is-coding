# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root,None)
        def dfs( node: Optional[TreeNode],  current_depth: int)-> Optional[TreeNode]:
            if not node:
                return 
            if current_depth == depth - 1:
                old_left = node.left
                old_right = node.right

                node.left = TreeNode(val, old_left, None)
                node.right = TreeNode(val, None, old_right)
                return
            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)
        dfs(root,1)
        return root