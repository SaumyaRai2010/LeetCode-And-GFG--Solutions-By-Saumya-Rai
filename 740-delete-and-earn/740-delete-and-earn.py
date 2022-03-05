class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=i
        dp=[0 for i in range(max(nums)+1)]
        dp[1]=d[1]
        for i in range(2,max(nums)+1):
            dp[i]=max(dp[i-1],dp[i-2]+d[i])
        print(dp)
        return dp[max(nums)]
    
        