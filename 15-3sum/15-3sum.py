class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        X = sorted(arr)
        i = 0
        j = i+1
        k = len(arr)-1
        Y = []
        while i < len(arr)-2:
            j = i+1
            k = len(arr)-1
            while j < k:
                if X[i]+X[j]+X[k]==0:
                    Y.append([X[i], X[j], X[k]])
                    j = j+1
                    k = k-1
                else:
                    if X[j]+X[k]+X[i]>0:
                        k = k-1
                    else:
                        j = j+1
            i = i+1

        Z=[]
        for i in Y:
            if i not in Z:
                Z.append(i)
        return Z
