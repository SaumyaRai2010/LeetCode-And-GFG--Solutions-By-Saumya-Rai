class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        d[0]=-1
        s=0
        for i in range(n):
            if nums[i]==0:
                nums[i]=-1
        maxx=0
        for i in range(n):
            s+=nums[i]
            if s in d:
                j=d[s]+1
                maxx=max(maxx,i-j+1)
            else:
                d[s]=i
        return maxx
            