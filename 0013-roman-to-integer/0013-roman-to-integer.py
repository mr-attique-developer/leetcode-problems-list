class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000

        }
        pre = 0 
        res = 0 

        for char in reversed(s):
            cur = roman[char]
            if cur < pre:
                res -=cur
            else:
                res += cur
            pre = cur
        return res
