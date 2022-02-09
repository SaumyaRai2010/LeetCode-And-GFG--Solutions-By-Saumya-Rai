class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        
        ans=0
        for i,j in d.items():
            if k==0:
                if j>1:
                    ans+=1
            else:
                if (k+i in d):
                    ans+=1
            # print(d,ans)    
        return ans
                
                
                
                
            