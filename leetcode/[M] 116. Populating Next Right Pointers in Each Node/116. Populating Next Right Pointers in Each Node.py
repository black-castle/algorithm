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
        if root == None: return root
        queue = list()
        queue.append(root)
        
        cnt, first, prv = 1, 1, None
        while len(queue) > 0:
            here = queue.pop(0)
            if cnt == first:    first = first * 2
            else:               prv.next = here
            
            prv, cnt = here, cnt + 1
            if here.left != None:
                queue.append(here.left)
                queue.append(here.right)
        
        return root            
            
        