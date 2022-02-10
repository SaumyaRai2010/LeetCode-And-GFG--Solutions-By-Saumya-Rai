from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left_sum=[]
        right_sum=[]
        s=0
        c=0
        for i in nums:
            s=s+i
            left_sum.append(s)
       
        d={}
        d[0]=1
        for i in left_sum:
            if i-k in d:
                c=c+d[i-k]
            if i not in d:
                d[i]=0
            d[i]=d[i]+1
            
            
        return c
            
            
            
        
                
            
        