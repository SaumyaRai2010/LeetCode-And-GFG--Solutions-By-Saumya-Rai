class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp=[0 for i in range(max(nums)+1)]
        for i in range(len(nums)):
            dp[nums[i]]+=nums[i]

        dp2=[0 for i in range(len(dp))]
        dp2[0]=dp[0]
        dp2[1]=max(dp[0],dp[1])
        for i in range(2,len(dp2)):
            dp2[i]=max(dp2[i-1],dp2[i-2]+dp[i])

        return max(dp2)
        
        