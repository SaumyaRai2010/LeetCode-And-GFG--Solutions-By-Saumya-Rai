#User function Template for python3
from collections import defaultdict
class Solution:
    def minTime(self, root,target):
        # code here
        d=defaultdict(set)
        def dfs(root):
            if root is None:
                return 
            if root.left:
                d[root.data].add(root.left.data)
                d[root.left.data].add(root.data)
                dfs(root.left)
            if root.right:
                d[root.data].add(root.right.data)
                d[root.right.data].add(root.data)
                dfs(root.right)
        queue=[[target,0]]
        visited={target}
        ans=0
        dfs(root)
        while queue:
            root,level=queue.pop(0)
            ans=max(ans,level)
            for i in list(d[root]):
                if i in visited:
                    continue
                visited.add(i)
                queue.append([i,level+1])
        return ans
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends