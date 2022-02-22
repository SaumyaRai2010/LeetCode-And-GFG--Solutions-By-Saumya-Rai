class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        i=intervals[0][0]
        j=intervals[0][1]
        cnt=0
        for interval in intervals[1:]:
            if i<=interval[0]<j and i<interval[1]<=j:
                cnt+=1
            i=interval[0]
            j=max(j,interval[1])
        return len(intervals)-cnt
            
            