class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n=len(seats)
        left=[0 for i in range(n)]
        right=[0 for i in range(n)]
        last=-1
        for i in range(n):
            if seats[i]==1:
                last=i
                left[i]=0
            else:
                if last==-1:
                    left[i]=last
                    continue
                left[i]=i-last
        next=-1
        for i in range(n-1,-1,-1):
            if seats[i]==1:
                next=i
                right[i]=0
            else:
                right[i]=next-i
        print(left,right)
        ans=0
        for i in range(n):
            if seats[i]==1:
                continue
            if right[i]<0:
                ans=max(ans,left[i])
            elif left[i]<0:
                ans=max(ans,right[i])
            else:
                ans=max(ans,min(right[i],left[i]))
                
        return ans