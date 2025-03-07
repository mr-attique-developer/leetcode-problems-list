class Solution:
    def repeatedCharacter(self, s: str) -> str:
        first = []
        for i in s:
            # print(i)
            if i in first:
                return i 
                print(first)
            first.append(i)    
        