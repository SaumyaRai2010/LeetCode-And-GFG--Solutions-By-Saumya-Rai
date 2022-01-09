class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        a=0
        b=0
        face='N'
        prev='N'
        for i in instructions:
            if i=='L':
                if face=='N':
                    face='W'
                elif face=='S':
                    face='E'
                elif face=='E':
                    face='N'
                else:
                    face='S'
            elif i=='R':
                if face=='N':
                    face='E'
                elif face=='S':
                    face='W'
                elif face=='E':
                    face='S'
                else:
                    face='N'
            else:
                if face=='N':
                    b+=1
                elif face=='S':
                    b-=1
                elif face=='W':
                    a-=1
                else:
                    a+=1
        print(a,b)
        if a==0 and b==0:
            return True
        if face!=prev:
            return True
        return False
                