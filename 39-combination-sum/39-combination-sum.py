class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def combo(arr,candidates,target,summ):
            if summ>target:
                return
            if summ==target:
                ans.append(arr)
                return
            for i in range(len(candidates)):
                combo(arr+[candidates[i]],candidates[i:],target,summ+candidates[i])
                
        combo([],candidates,target,0)
        return ans
        
            