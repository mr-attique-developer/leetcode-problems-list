class Solution:
    def finalString(self, s: str) -> str:
        res = []

        for i in s: 
            if i == "i":
                left = 0
                right = len(res) - 1
                while left < right:
                    res[left], res[right] = res[right], res[left]
                    left += 1
                    right -= 1
            else:
                res.append(i)
        return "".join(res)