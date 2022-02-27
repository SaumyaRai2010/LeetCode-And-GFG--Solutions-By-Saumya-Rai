class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i]=0
            d1[i]+=1
        print(sorted(s))
        for j in t:
            if j not in d2:
                d2[j]=0
            d2[j]+=1
        print(d1,d2)
        same=0
        for i,j in d1.items():
            if i in d2:
                same+=min(d2[i],j)
        
        
        return len(s)+len(t)-2*same