class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp1=[0 for i in range(n)]
        dp2=[0 for i in range(n)]
        if n<=3:
            return max(nums)
        for i in range(len(nums)-1):
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i])
        for i in range(1,len(nums)):
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums[i])
        
        # print(dp)
        return max(max(dp1),max(dp2))
        