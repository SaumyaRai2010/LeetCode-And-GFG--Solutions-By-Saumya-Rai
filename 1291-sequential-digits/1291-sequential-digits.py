class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s='123456789'
        ans=[]
        for i in range(len(s)):
            for j in range(len(s)+1):
                # print(s[i:j])
                if s[i:j]!='' and int(s[i:j])>=low and int(s[i:j])<=high:
                    ans.append(int(s[i:j]))
        return sorted(ans)
            