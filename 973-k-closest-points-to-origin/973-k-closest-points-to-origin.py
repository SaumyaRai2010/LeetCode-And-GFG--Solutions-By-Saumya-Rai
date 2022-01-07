import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        heapq.heapify(heap)
        for i in range(len(points)):
            a=points[i][0]
            b=points[i][1]  
            heapq.heappush(heap,(-(a**2+b**2),[a,b]))
            if i>=k:
                heapq.heappop(heap)
        ans=[]
        for i,j in heap:
            ans.append(j)
        return ans