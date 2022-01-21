import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=0
            d[i]+=1
        ans=[]
        heap=[]
        heapq.heapify(heap)
        for i,j in d.items():
            heapq.heappush(heap,(j,i))
        
        while heap:
            val=heapq.heappop(heap)
            ans.append(val[0]*val[1])
        ans=ans[::-1]
        return ''.join(ans)