class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for num in s:
            if num.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(num)
        return "".join(stack)                  

                