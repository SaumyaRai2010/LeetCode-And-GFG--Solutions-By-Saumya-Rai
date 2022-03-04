# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        queue=[[root,0]]
        next=[]
        while queue:
            val=queue[0]
            start=queue[0][1]
            end=queue[-1][1]
            ans=max(ans,end-start+1)
            for i in queue:
                if i[0].left:
                    next.append([i[0].left,2*i[1]+1])
                if i[0].right:
                    next.append([i[0].right,2*i[1]+2])
            queue.pop(0)
            queue=next
            next=[]
        return ans
            