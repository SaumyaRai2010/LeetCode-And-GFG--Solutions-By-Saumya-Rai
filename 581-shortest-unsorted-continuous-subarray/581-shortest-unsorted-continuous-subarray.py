class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i=0
        while i<len(nums)-1:
            if nums[i+1]>=nums[i]:
                i=i+1
            else:
                break

        j=len(nums)-1
        while j>0:
            if nums[j-1]<=nums[j]:
                j=j-1
            else:
                break
        if i==len(nums)-1:
            return 0
        maxx=max(nums[i:j+1])
        minn=min(nums[i:j+1])
        #Now we check in the subarray before the starting index
        while i>0:
            if nums[i-1]>minn:
                i=i-1
            else:
                break
        while j<len(nums)-1:
            if nums[j+1]<maxx:
                j=j+1
            else:
                break
        
        
        return j-i+1
        
        