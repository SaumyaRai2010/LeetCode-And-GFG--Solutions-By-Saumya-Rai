class Solution:
    def trap(self, height: List[int]) -> int:
        left=[]
        right=[]
        lmax=-1
        rmax=-1
        for i in range(len(height)):
            lmax=max(lmax,height[i])
            left.append(lmax)
        for i in range(len(height)-1,-1,-1):
            rmax=max(rmax,height[i])
            right.append(rmax)
        right=right[::-1]
        
        ans=0
        for i in range(len(height)):
            ans+=min(left[i],right[i])-height[i]
        return ans