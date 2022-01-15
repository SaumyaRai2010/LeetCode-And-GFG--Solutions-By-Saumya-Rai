class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        print(s)
        cnt=s.count('')
        ans=['' for i in range(len(s)-cnt)]
        pos=0
        for i in s:
            if i!='':
                ans[pos]=i
                pos+=1
        ans=ans[::-1]
        return ' '.join(ans)
        