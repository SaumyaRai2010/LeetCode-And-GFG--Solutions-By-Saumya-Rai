# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 
        ans=[]
        queue=[root]
        next=[]
        curr=[]
        while queue!=[]:
            for i in queue:
                curr.append(i.val)
                if i.left:
                    next.append(i.left)
                if i.right:
                    next.append(i.right)
            ans.append(curr)
            queue=next
            next=[]
            curr=[]
        return ans