class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        ans=[]
        i=len(a)-1
        j=len(b)-1
        while j>-1 and i>-1:
            if a[i]=='1' and b[j]=='1':
                if carry==1:
                    ans.append('1')
                else:
                    ans.append('0')
                    carry=1
            elif a[i]=='0' and b[j]=='0':
                if carry==1:
                    ans.append('1')
                    carry=0
                else:
                    ans.append('0')
            elif a[i]=='0' and b[j]=='1':
                if carry==1:
                    ans.append('0')
                    carry=1
                else:
                    ans.append('1')
                    carry=0
            elif a[i]=='1' and b[j]=='0':
                if carry==1:
                    ans.append('0')
                else:
                    ans.append('1')
            i-=1
            j-=1

        while i!=-1:
                if a[i]=='1':
                    if carry==1:
                        ans.append('0')
                    else:
                        ans.append('1')
                        carry=0
                else:
                    if carry==1:
                        ans.append('1')
                        carry=0
                    else:
                        ans.append('0')
                i-=1
        while j!=-1:
                if b[j]=='1':
                    if carry==1:
                        ans.append('0')
                    else:
                        ans.append('1')
                        carry=0
                else:
                    if carry==1:
                        ans.append('1')
                        carry=0
                    else:
                        ans.append('0')
                j-=1
        if carry==1:
            ans.append('1')
        ans=ans[::-1]
        print(ans)
        return ''.join(ans)

            
                    
        
                    