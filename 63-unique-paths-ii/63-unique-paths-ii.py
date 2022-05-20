class Solution:
    def uniquePathsWithObstacles(self, arr: List[List[int]]) -> int:
        dp=[[0 for i in range(len(arr[0]))] for j in range(len(arr))]
        for i in range(len(arr)):
            if arr[i][0]==1:
                break
            dp[i][0]=1
        for i in range(len(arr[0])):
            if arr[0][i]==1:
                break
            dp[0][i]=1
            
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if arr[i][j]==1:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                
        return dp[-1][-1]
                
        
        
            