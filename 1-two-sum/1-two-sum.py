class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nlist=nums.copy()
        nums.sort()
        i=0
        arr=[]
        j=len(nums)-1
        while i<j:
            if (nums[i]+nums[j])>target:
                j=j-1
                
            elif (nums[i]+nums[j])<target:
                i=i+1
            else:
                a=nums[i]
                b=nums[j]
                break
        if nums[i]==nums[j]:
            arr.append(nlist.index(a))
            arr.append(nlist.index(b,arr[0]+1))
            return arr
        pos1=nlist.index(nums[i])
        pos2=nlist.index(nums[j])
        return[pos1,pos2]
                  
            