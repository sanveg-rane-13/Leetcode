# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invertNodeChildren(root)
        return root
        
    def invertNodeChildren(self, node: TreeNode):
        # stopping condition
        if not node:
            return
        
        # swap the children of current node
        temp = node.left
        node.left = node.right
        node.right = temp
        
        # recurssively check for left and right children of current node
        self.invertNodeChildren(node.left)
        self.invertNodeChildren(node.right)