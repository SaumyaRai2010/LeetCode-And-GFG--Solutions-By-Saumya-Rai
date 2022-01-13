class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        i=len(prices)-1
        val=prices[i]
        while i>0:
            if prices[i-1]>val:
                val=prices[i-1]
            else:
                s=s+val-prices[i-1]
                val=prices[i-1]
            i=i-1
        return s