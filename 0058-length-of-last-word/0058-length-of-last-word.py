class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split()[-1]
        return len(split)