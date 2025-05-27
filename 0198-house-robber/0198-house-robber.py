class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(maxsize=None)
        def dp(i):
            if i >= n:
                return 0
            rob = nums[i] + dp(i+2)
            skip = dp(i + 1)
            return max(rob, skip)
        return dp(0)