class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        s=s.split(' ')
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]]=s[i]
            else:
                if d[pattern[i]]!=s[i]:
                    return False
        d2={}
        for i in range(len(pattern)):
            if s[i] not in d2:
                d2[s[i]]=pattern[i]
            else:
                if d2[s[i]]!=pattern[i]:
                    return False
        return True