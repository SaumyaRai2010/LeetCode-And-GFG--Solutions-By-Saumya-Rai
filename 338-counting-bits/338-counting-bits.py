class Solution:
    def countBits(self, n: int) -> List[int]:
        X=[]
        for i in range(0,n+1):
            X.append(i)
        print(X)
        ans=[0 for i in range(n+1)]
        for i in range(0,len(X)):
            t=X[i]
            while t>0:
                if (t&1)==1:
                    ans[i]=ans[i]+1
                t=t>>1
        return ans
            
        