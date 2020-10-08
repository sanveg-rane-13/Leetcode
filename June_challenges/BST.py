# Insert into a Binary Search Tree

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        q = [root]
        
        while q:
            h = q.pop(0)
            
            if val>=h.val:
                if h.right:
                    q.append(h.right)
                else:
                    h.right = TreeNode(val)
                    return root
            
            if val<h.val:
                if h.left:
                    q.append(h.left)
                else:
                    h.left = TreeNode(val)
                    return root