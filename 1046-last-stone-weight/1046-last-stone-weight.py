import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        if len(stones)==2:
            return abs(stones[0]-stones[1])
        heap=[]
        heapq.heapify(heap)
        for i in stones:
            heapq.heappush(heap,-1*i)
            

        
        while len(heap)>1:
            val1=-1*heapq.heappop(heap)
            val2=-1*heapq.heappop(heap)
            if val1==val2:
                ans=0
            else:
                ans=abs(val1-val2)
            heapq.heappush(heap,-1*ans)
        return ans