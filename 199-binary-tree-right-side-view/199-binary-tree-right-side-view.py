# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans=[]
        d={}
        def dfs(root,level):
            if root is None:
                return
            if level not in d:
                d[level]=root
            right=dfs(root.right,level+1)
            left=dfs(root.left,level+1)
        dfs(root,0)
        for i in sorted(d):
            ans.append(d[i].val)
        return ans