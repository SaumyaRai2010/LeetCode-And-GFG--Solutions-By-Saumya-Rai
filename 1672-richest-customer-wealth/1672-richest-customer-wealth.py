class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx=0
        for i in accounts:
            if maxx<sum(i):
                maxx=sum(i)
        return maxx