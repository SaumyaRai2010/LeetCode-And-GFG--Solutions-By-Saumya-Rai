class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        ans=[]
        n=len(digits)
        if len(digits) ==0:
            return ans
        def func(curr,pos):
            if pos>=n:
                ans.append(curr)
                return
            index=int(digits[pos])
            val=arr[index]
            for i in val:
                func(curr+i,pos+1)
        func('',0)
        return ans
                
                
                
                