class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in s:
            if stack and i==')' and stack[top]=='(':
                stack.pop()
                top=top-1
            elif stack and i=='}' and stack[top]=='{':
                stack.pop()
                top=top-1
            elif stack and i==']' and stack[top]=='[':
                stack.pop()
                top=top-1
            else:
                stack.append(i)
                top=top+1
            # print(stack)
        if not stack:
            return True
        return False
            