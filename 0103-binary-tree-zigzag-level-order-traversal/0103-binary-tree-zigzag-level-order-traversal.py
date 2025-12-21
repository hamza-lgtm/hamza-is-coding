# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = list()
        queue = deque([root])
        zig = True
        while queue :
            vals = []
            n = len(queue)
            
            for _ in range(n):
                node = queue.popleft()
                vals.append(node.val)
                if zig:
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            zig = not zig   
            result.append(vals)
        return result

        