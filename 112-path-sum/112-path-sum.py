# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,s):
            if root is None:
                return None
            s+=root.val
            if s==targetSum and root.left is None and root.right is None:
                return True
            left=dfs(root.left,s)
            right=dfs(root.right,s)
            return left or right
            
        return dfs(root,0)