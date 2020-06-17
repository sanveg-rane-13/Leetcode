# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.sol = None
        self.traverseTree(root, val)

        return self.sol
    
    def traverseTree(self, node, val):
        if not node or self.sol != None:
            return
        
        if node.val == val:
            self.sol = node
            return
        
        self.traverseTree(node.left, val)
        self.traverseTree(node.right, val)