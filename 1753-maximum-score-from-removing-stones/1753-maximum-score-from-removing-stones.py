import heapq
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap=[]
        heapq.heapify(heap)
        heapq.heappush(heap,-a)
        heapq.heappush(heap,-b)
        heapq.heappush(heap,-c)
        ans=0
        while len(heap)>1:
            val1=-1*heapq.heappop(heap)
            val2=-1*heapq.heappop(heap)
            val1-=1
            val2-=1
            ans+=1
            if val1==0 and val2==0:
                break
            elif val1==0:
                heapq.heappush(heap,-val2)
            elif val2==0:
                heapq.heappush(heap,-val1)
            else:
                heapq.heappush(heap,-val1)
                heapq.heappush(heap,-val2)
        return ans
            