# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        r = list()
        r.append([root.val])
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            t= []
            if node.left:
                t.append(node.left.val)
                queue.append(node.left)
            if node.right:
                t.append(node.right.val)
                queue.append(node.right)
            if t:
                r.append(t)
        return r

            

        