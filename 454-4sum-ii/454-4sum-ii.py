from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        c=0
        d1=defaultdict(lambda:0)
        d2=defaultdict(lambda:0)
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                x=nums1[i]+nums2[j]
                d1[x]=d1[x]+1
        for i in range(0,len(nums3)):
            for j in range(0,len(nums4)):
                x=nums3[i]+nums4[j]
                d2[x]=d2[x]+1
        for i in d1:
            j=i*(-1)
            if (j) in d2:
                k=d1[i]*d2[j]
                c=c+k
        return c
        
        
        
                    
                        
        
                            
            
        