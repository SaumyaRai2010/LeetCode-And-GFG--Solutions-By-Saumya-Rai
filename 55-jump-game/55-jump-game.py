class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        maxx=i+nums[0]
        n=len(nums)
        while i<n-1:
            if i>maxx:
                return False
            maxx=max(maxx,i+nums[i])
            i+=1
        if maxx<n-1:
            return False
        return True