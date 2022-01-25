class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i=1
        n=len(arr)
        if len(arr)<=2:
            return False
        while i<n-1:
            if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
                start=i-1
                end=i+1
                while start>0 and arr[start-1]<arr[start] :
                    start-=1
                while end<n-1 and arr[end+1]<arr[end]:
                    end+=1
                print(end,start)
                if end==n-1 and start==0:
                    return True
            i+=1
        return False