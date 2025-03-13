from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Finding first positive number
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > 0:
                r = mid - 1
            else:
                l = mid + 1
        positive_count = n - l  # Count of positive numbers

        # Finding first non-negative number (0 or positive)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
        negative_count = l  # Count of negative numbers

        return max(positive_count, negative_count)
