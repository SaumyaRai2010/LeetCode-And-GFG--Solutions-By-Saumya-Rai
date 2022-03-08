#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        ans=0
        i=0
        j=0
        arr.sort()
        dep.sort()
        maxx=0
        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                i+=1
                ans+=1
                maxx=max(maxx,ans)
            else:
                j+=1
                
                ans-=1
        return maxx
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends