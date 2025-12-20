"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return

        queue = deque([root])
        
        while queue:
            level_len = len(queue)
            prev_node = None
           
            for _ in range(level_len):
                node = queue.popleft()
                if prev_node :
                    prev_node.next = node
                prev_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            prev_node.next = None
        return root


            


        