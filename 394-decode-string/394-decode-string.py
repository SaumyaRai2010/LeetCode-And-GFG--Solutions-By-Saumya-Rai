class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        ans=[]
        for i in range(len(s)):
            if s[i]==']':
                test=''
                while stack[-1]!='[':
                    val=stack.pop()
                    test=test+val[::-1]
                stack.pop()
                rev=test[::-1]
                num=''
                while stack and stack[-1] in '0123456789':
                    val=stack.pop()
                    num=num+val
                num=num[::-1]
                cnt=int(num)
                stack.append(cnt*(rev))
            else:
                stack.append(s[i])
        return ''.join(stack)
                