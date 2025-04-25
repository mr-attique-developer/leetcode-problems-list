class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == ")" and len(stack) > 0 and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)