class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i=0
        arr=[]
        X=[]
        def helper(nums,i,arr,X):
            if i==len(nums):
                X.append(arr[:])
                return
            helper(nums,i+1,arr,X)
            arr.append(nums[i])
            helper(nums,i+1,arr,X)
            arr.pop()
        helper(nums,i,arr,X)
        return X