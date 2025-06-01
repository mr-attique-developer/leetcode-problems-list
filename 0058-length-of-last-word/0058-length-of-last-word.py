class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words_array = s.split()
        length = len(words_array.pop())
        return length 