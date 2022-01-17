class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0 for i in range(n+1)]
        for i in range(n-1,-1,-1):
            dp[i]=max(questions[i][0]+dp[min(n,i+questions[i][1]+1)],dp[i+1])
        return dp[0]