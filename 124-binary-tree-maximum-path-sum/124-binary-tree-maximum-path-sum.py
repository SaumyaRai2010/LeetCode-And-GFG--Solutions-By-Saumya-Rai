# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=[-float('inf')]
        def dfs(root):
            if root is None:
                return 0
            left=max(0,dfs(root.left))
            right=max(0,dfs(root.right))
            ans[0]=max(left+right+root.val,root.val,ans[0])
            return max(left,right)+root.val
        dfs(root)
        return ans[0]