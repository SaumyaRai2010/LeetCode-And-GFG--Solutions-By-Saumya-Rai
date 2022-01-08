class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        itr=0
        while itr<=high:
            if nums[itr]==0:
                nums[low],nums[itr]=nums[itr],nums[low]
                itr+=1
                low+=1
            elif nums[itr]==2:
                nums[itr],nums[high]=nums[high],nums[itr]
                high-=1
            else:
                itr+=1
            