class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length=len(flowerbed)
        if n==0:
            return True
        if length==1:
            if flowerbed[0]==0:
                return True
            return False
        for i in range(length):
            if flowerbed[i]==0:
                if i==0:
                    if (flowerbed[0]==0 and flowerbed[1]==0):
                        n-=1
                        flowerbed[0]=1
                elif i==length-1:
                    if (flowerbed[length-1]==0 and flowerbed[length-2]==0):
                        n-=1
                        flowerbed[length-1]=1
                else:
                    if (flowerbed[i-1]==0 and flowerbed[i+1]==0):
                        n-=1
                        flowerbed[i]=1
            print(i,n)
            if n==0:
                return True
        return False
                    
        