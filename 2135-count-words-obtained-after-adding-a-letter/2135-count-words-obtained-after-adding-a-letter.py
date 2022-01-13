class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        s=set()
        for i in startWords:
            s.add(''.join(sorted(i)))
        ans=0
        for i in targetWords:
            if len(i)>1:
                val=''.join(sorted(i))
                for j in range(len(val)):
                    temp=val[:j]+val[j+1:]
                    if temp in s:
                        ans+=1
                        break
        return ans
                    
        