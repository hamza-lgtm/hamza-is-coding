"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            level_len = len(queue)
            t = []
            for _ in range(level_len):
                node = queue.popleft()
            
                t.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(t)
        return result
            
                

        