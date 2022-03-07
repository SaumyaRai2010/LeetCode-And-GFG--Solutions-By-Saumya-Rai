# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        ans=[]
        d=defaultdict(list)
        def hashing(root):
            if root is None:
                return
            if root.right:
                d[root.right.val].append((root.val,"U"))
                d[root.val].append((root.right.val,"R"))
                hashing(root.right)
            if root.left:
                d[root.left.val].append((root.val,"U"))
                d[root.val].append((root.left.val,"L"))
                hashing(root.left)
        hashing(root)
        queue=[]
        queue.append([startValue,""])
        visited=set()
        visited.add(startValue)
        while queue:
            root,path=queue.pop(0)
            if root==destValue:
                return path
            for i in d[root]:
                if i[0] in visited:
                    continue
                visited.add(i[0])
                queue.append([i[0],path+i[1]])
        return path
                
                
                