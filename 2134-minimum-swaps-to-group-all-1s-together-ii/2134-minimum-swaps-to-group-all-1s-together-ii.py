class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one=nums.count(1)
        nums.extend(nums)
        maxx=0
        x=0
        for i in range(len(nums)):
            if i>=one and nums[i-one]==1:
                x-=1
            if nums[i]==1:
                x+=1
            maxx=max(maxx,x)
        return one-maxx
                
                    