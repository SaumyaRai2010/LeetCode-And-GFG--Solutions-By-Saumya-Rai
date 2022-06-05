class Solution:
    def totalNQueens(self, n: int) -> int:
            def checker(arr,row,col,N):
                for i in range(N):
                    if arr[i][col]=="Q":
                        return False
                i=row
                j=col
                #upper left
                while row>0 and col>0:
                    row-=1
                    col-=1
                    if arr[row][col]=="Q":
                        return False
                #upper right
                while i>0 and j<N-1:
                    i=i-1
                    j+=1
                    if arr[i][j]=="Q":
                        return False
                return True

            def queen(arr,row,X):
                if row==len(arr):
                    ans=[]
                    for a in arr:
                        ans.append("".join(a))
                    X.append(ans)
                    return True
                for i in range(len(arr)):
                    if checker(arr,row,i,len(arr)):
                        arr[row][i]="Q"
                        queen(arr,row+1,X)
                        arr[row][i]="."
                return False



            arr=[['.' for i in range(n)] for j in range(n)]
            row=0
            col=0
            X=[]
            queen(arr,row,X)
            return len(X)