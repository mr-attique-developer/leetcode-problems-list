class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            s_count = s.count(i)
            t_count = t.count(i)
            if s_count != t_count:
                return i
          