class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j=len(s)-1
        count=0
        if not s:
            return False

        while i <=j:
            if s[i]==s[j]:
                j-=1
            elif s[i] !=s[j]:
              return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
            i+=1
        return True