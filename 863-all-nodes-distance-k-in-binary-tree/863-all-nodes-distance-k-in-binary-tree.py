# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d=defaultdict(set)
        def dfs(root):
            if root.right:
                d[root.val].add(root.right.val)
                d[root.right.val].add(root.val)
                dfs(root.right)
            if root.left:
                d[root.val].add(root.left.val)
                d[root.left.val].add(root.val)
                dfs(root.left)
        dfs(root)
        queue=[[target.val,0]]
        visited={target.val}
        ans=[]
        while queue:
            i,j = queue.pop(0)
            if j==k:
                ans.append(i)
            for value in list(d[i]):
                if value in visited:
                    continue
                visited.add(value)
                queue.append([value,j+1])

            
        return ans