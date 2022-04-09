import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        heap=[]
        heapq.heapify(heap)
        pos=0
        for i,j in d.items():
            heapq.heappush(heap,(j,i))
            pos+=1
            if pos>k:
                heapq.heappop(heap)
        ans=[]
        while heap:
            val=heapq.heappop(heap)
            ans.append(val[1])
        return ans
        
            
        