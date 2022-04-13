class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        k=n*n
        i=0
        r=0
        X=[[0 for a in range(n)] for j in range(n)]
        d=len(X)-1
        l=len(X[0])-1
        u=len(X)-1
        while i<n*n:
            for a in range(r,l+1):
                X[r][a]=i+1
                i=i+1
            if i==n*n:
                break
            for a in range(r+1,d+1):
                X[a][l]=i+1
                i=i+1
            if i==n*n:
                break
            for a in range(l-1,r-1,-1):
                X[u][a]=i+1
                i=i+1
            if i==n*n:
                break
            for a in range(u-1,r,-1):
                X[a][r]=i+1
                i=i+1
            if i==n*n:
                break
            r=r+1
            u=u-1
            d=d-1
            l=l-1
        return X
                
        