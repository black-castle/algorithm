# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cases = []
    def trip(self, node: Optional[TreeNode], num : int) -> list:
        if node is None:
            return
        num = num * 10 + node.val
        if node.left == None and node.right == None:
            self.cases.append(num)
        else:
            self.trip(node.left, num)
            self.trip(node.right, num)
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.cases.clear()
        self.trip(root, 0)
        sum = 0
        for case in self.cases:
            sum += int(str(case), 2)
        return sum