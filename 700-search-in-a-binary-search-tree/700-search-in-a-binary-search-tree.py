# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        arr=[]
        def dfs(root):
            if root is None:
                return None
            if root.val==val:
                arr.append(root)
                return root
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        if not arr:
            return None
        return arr[0]
            