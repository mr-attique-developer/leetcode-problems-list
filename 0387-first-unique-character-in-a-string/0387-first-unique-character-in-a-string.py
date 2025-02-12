class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            found = False
            for  j in range(len(s)):
                if i != j and s[i] == s[j]:
                    found = True
                    break
                
            if not found:
                    return i 
        return -1
