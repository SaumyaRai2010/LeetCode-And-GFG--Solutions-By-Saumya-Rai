# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        queue=[root]
        curr=[]
        next=[]
        flag=-1
        if not root:
            return []
        while queue:
            for i in queue:
                curr.append(i.val)
                if i.left:
                    next.append(i.left)
                if i.right:
                    next.append(i.right)
            if flag==1:
                curr=curr[::-1]
            ans.append(curr)
            flag=flag*(-1)
            queue=next
            curr=[]
            next=[]
        return ans
                