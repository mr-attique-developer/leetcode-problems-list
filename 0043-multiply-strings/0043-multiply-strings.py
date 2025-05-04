class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def toDigit(num:str)->int:
            dig = 0
            for c in num:
                dig = dig  * 10 + ord(c) - ord("0")
            return dig
        return str(toDigit(num1) * toDigit(num2))