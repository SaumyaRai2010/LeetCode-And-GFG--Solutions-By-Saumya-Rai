class Solution:
    def candy(self, A: List[int]) -> int:
        n=len(A)
        dp=[1 for i in range(n)]
        for i in range(n-1):
            if A[i+1]>A[i]:
                dp[i+1]=dp[i]+1
        
        for i in range(n-1,0,-1):
            if A[i-1]>A[i] and dp[i-1]<=dp[i]:
                dp[i-1]=dp[i]+1
        return sum(dp)