class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        n1=len(s1)
        n2=len(s2)
        d1={}
        d2={}
        for i in s1:
            if i not in d1:
                d1[i]=0
            d1[i]+=1
        i=0
        start=0
        while i<n2:
            if i<n1:
                if s2[i] not in d2:
                    d2[s2[i]]=0
                d2[s2[i]]+=1
                i+=1
            else:
                if s2[i] not in d2:
                    d2[s2[i]]=0
                d2[s2[i]]+=1
                d2[s2[start]]-=1
                if d2[s2[start]]==0:
                    del d2[s2[start]]
                start+=1
                i+=1
            if d2==d1:
                    return True
            # print(d2)
        return False
        