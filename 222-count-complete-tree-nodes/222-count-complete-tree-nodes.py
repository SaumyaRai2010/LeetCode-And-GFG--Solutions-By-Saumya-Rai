# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def dfs(root):
            if root is None:
                return
            ans[0]=ans[0]+1
            left=dfs(root.left)
            right=dfs(root.right)
        dfs(root)
        return ans[0]