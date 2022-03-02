class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        n1=len(s)
        n2=len(t)
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        if i==n1:
            return True
        return False