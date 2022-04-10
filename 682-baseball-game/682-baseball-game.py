class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in ops:
            if i=='D':
                val=2*int(stack[-1])
                stack.append(val)
            elif i=='C':
                stack.pop()
            elif i=='+':
                a=stack[-1]
                b=stack[-2]
                stack.append(int(a)+int(b))
            else:
                stack.append(i)
        s=0
        print(stack)
        for i in stack:
            s+=int(i)
        return s