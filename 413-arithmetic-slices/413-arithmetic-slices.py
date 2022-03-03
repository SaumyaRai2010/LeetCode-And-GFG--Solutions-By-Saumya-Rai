class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        i=1
        while i<n:
            cnt=1
            val=nums[i]-nums[i-1]
            while i<n and nums[i]-nums[i-1]==val:
                cnt+=1
                i+=1
            if cnt>=3:
                ans=ans+(cnt-1)*(cnt-2)//2
        return ans
            
            