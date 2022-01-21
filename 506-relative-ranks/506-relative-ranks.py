import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=['' for i in range(len(score))]
        flag=1
        heap=[]
        heapq.heapify(heap)
        for i in range(len(score)):
            heapq.heappush(heap,(-1*score[i],i))
        # print(heap)
        while heap:
            val=heapq.heappop(heap)
            # print(val)
            if flag==1:
                ans[val[1]]='Gold Medal'
            elif flag==2:
                ans[val[1]]='Silver Medal'
            elif flag==3:
                ans[val[1]]='Bronze Medal'
            else:
                ans[val[1]]=str(flag)
            flag+=1
        return ans