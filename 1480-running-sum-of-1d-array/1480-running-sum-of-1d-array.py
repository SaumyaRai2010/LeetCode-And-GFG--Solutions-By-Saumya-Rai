class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        left=[]
        s=0
        for i in nums:
            s+=i
            left.append(s)
        return left