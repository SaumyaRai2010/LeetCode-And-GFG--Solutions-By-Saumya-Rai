class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp={}
        ds={}
        for i in p:
            if i not in dp:
                dp[i]=0
            dp[i]+=1
        ans=[]
        lenp=len(p)
        lens=len(s)
        i=0
        while i<lens:
            if i>=lenp-1:
                if s[i] not in ds:
                    ds[s[i]]=0
                ds[s[i]]+=1
                if ds==dp:
                    ans.append(i-lenp+1)
                   
                
                ds[s[i-lenp+1]]-=1
                if ds[s[i-lenp+1]]==0:
                    del ds[s[i-lenp+1]]
                i+=1

            else:
                if s[i] not in ds:
                    ds[s[i]]=0
                ds[s[i]]+=1
                i+=1
            # print(ds,dp)
        return ans