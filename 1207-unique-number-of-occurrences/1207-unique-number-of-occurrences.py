class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d1={}
        for i in arr:
            if i not in d1:
                d1[i]=0
            d1[i]+=1
        
        d2={}
        for i,j in d1.items():
            if j not in d2:
                d2[j]=i
            else:
                return False
        return True