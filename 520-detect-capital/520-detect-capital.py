class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if ord(word[0])>=65 and ord(word[0])<=90:
            i=1
            n=len(word)
            while i<n:
                    if ord(word[i])>90:
                        i+=1
                    else:
                        break
            
            if i==n:
                return True
            i=1
            while i<n:
                if ord(word[i])>90:
                    return False
                i+=1
                
            return True
        else:
            i=0
            n=len(word)
            while i<n:
                if ord(word[i])>=65 and ord(word[i])<=90:
                    return False
                i+=1
            return True