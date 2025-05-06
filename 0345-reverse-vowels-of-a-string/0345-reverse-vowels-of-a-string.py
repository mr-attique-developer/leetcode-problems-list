class Solution:
    def reverseVowels(self, s: str) -> str:
        res = ""
        stack = []

        vol = "aeiouAEIOU"
        for i in s:
            if i in vol:
                stack.append(i)
        for i in s:
            if i in vol:
                res += stack.pop()
            else:
                res += i
        return res