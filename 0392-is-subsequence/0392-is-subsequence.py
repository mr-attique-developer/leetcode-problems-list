class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if s == "":
            return True
        if len(s) > len(t):
            return False
        for i  in range(len(t)):
            if s[j] == t[i]:
                if j == len(s) - 1:
                    return True
                else:
                    j += 1
        return False
