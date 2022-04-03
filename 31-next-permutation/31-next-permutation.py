class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        n=len(nums)
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            nums.reverse()
            return
        k=i-1
        j=len(nums)-1
        while nums[k]>=nums[j]:
            j-=1
        nums[k],nums[j]=nums[j],nums[k]
        j=len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        