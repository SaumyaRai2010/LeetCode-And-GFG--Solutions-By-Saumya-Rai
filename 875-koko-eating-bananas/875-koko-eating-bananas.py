import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            s=0
            for i in piles:
                s+=math.ceil(i/mid)
            if s>h:
                low=mid+1
            else:
                high=mid-1
        return low
        
        