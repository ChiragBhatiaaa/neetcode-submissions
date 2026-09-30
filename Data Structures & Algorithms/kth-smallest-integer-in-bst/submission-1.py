# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        nodes_processed = 0 

        while root or stack: 
            while root: 
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            nodes_processed += 1

            if nodes_processed == k:
                return node.val 
            
            root = node.right
        