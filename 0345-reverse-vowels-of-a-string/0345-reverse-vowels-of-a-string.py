class Solution:
    def reverseVowels(self, s: str) -> str:
        res = ""
        vowels = "aeiouAEIOU"
        stack = []
        for i in s:
            if i in vowels:
                stack.append(i)
        for i in s:
            if i in vowels:
                res += stack.pop()
            else:
                res += i
        return res