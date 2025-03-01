class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
        # left = 0
        # right = len(s) - 1
        # while left <= right:
        #     if s[left] != s[right]:
        #         return 2
        #     left += 1
        #     right -= 1
        # return 1