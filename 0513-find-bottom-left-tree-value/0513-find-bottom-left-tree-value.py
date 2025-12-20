# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        leftmost = root.val
        while queue:
            level_len= len(queue)
            for i  in range(level_len):
                node = queue.popleft()
                if i == 0:
                    leftmost =node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return leftmost




    

        