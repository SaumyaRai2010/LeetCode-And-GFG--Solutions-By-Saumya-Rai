# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def dfs(root,arr):
            if root is None:
                return
            if root.left is None and root.right is None:
                ans.append(arr[::]+[str(root.val)])
                return
            else:
                left=dfs(root.left,arr+[str(root.val)])
                right=dfs(root.right,arr+[str(root.val)])
        dfs(root,[])
        return [ *map('->'.join, ans) ]