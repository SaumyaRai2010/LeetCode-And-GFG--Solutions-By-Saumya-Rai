class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        i=0
        X=[]
        def passing(s,i,j):
            test=s.copy()
            test[j],test[i]=test[i],test[j]
            return test
        def perm(s,i,X):
            if i==len(s):
                if s not in X:
                    X.append(s)
                return
            for k in range(i,len(s)):
                temp=passing(s,i,k)
                perm(temp,i+1,X)
        perm(nums,i,X)
        return X