class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pos=0
        if sum(cost)>sum(gas):
            return -1
        curr=0
        for i in range(len(gas)):
            curr=curr+gas[i]-cost[i]
            print(curr,i)
            if curr<0:
                pos=i+1
                curr=0
        return pos