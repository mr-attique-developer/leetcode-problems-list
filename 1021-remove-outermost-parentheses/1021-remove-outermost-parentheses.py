class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stack = []
        for i in s:
            if i == "(":
                if stack:
                    result.append(i)
                stack.append(i)
            if i == ")":
                stack.pop()
                if stack:
                    result.append(i)
                    

            
        return "".join(result)