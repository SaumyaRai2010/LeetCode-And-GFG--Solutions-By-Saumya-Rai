class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        arr=[1,2,3,4,5,6,7,8,9]
        def combo(summ,arr,curr,pos):
            if summ>n or len(curr)>k:
                return 
            if summ==n and len(curr)==k:
                ans.append(curr)
                return
            for i in range(pos,len(arr)):
                combo(summ+arr[i],arr,curr+[arr[i]],i+1)
        
        combo(0,arr,[],0)
        return ans