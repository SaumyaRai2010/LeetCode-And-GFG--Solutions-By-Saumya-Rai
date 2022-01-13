class Solution:
    def maxProduct(self, A: List[int]) -> int:
        maxx_pro=A[0]
        ans=A[0]
        minn_pro=A[0]
        for i in range(1,len(A)):
            curr_max=max(A[i],maxx_pro*A[i],minn_pro*A[i])
            curr_min=min(A[i],maxx_pro*A[i],minn_pro*A[i])
            ans=max(ans,curr_max)
            maxx_pro=curr_max
            minn_pro=curr_min
        return ans