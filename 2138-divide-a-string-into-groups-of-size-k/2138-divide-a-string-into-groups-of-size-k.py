class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)//k
        if len(s)%k!=0:
            n+=1
        ans=['' for i in range(n)]
        pos=0
        
        for i in range(len(s)):
            if i!=0 and i%k==0:
                pos+=1
            ans[pos]=ans[pos]+s[i]
            # print(ans)
        while len(ans[-1])!=k:
            ans[-1]=ans[-1]+fill
        return ans