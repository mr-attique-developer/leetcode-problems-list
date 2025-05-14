class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_word = []
        for i in words:
            reverse = i[::-1]
            reverse_word.append(reverse)
        return " ".join(reverse_word)
