class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i in range(len(s)):
            last[s[i]]=i
        
        ans=[]
        maxReach=0
        val=0
        for i in range(len(s)):
            maxReach=max(maxReach,last[s[i]])
            val+=1
            if i==maxReach:
                ans.append(val)
                val=0
        return ans
        