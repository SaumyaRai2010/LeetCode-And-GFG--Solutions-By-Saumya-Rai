class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        i=0
        res=0
        sign=1
        ans=0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in '+-':
            sign = 1 if s[i] == '+' else -1
            i += 1
        while(i < len(s) and s[i].isdigit()):
            ans=ans * 10 + int(s[i])
            i+=1
        ans=ans*sign
        if ans>2**31-1:
            return 2**31-1
        elif ans<(-1*(2**31)):
            return -1*(2**31)
        return ans
        