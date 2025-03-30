class Solution:
    def minLength(self, s: str) -> int:
        arr = []
        for i in s:
            if arr and (arr[-1] == "A" and i == "B" or arr[-1] =="C" and i == "D"):
                arr.pop()
            else:
                arr.append(i)
        return len(arr)