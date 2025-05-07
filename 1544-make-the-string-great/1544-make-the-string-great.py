class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for val in s:
            if stack and abs(ord(stack[-1])  - ord(val)) == 32:
                stack.pop()
            else:
                stack.append(val)
        return "".join(stack)