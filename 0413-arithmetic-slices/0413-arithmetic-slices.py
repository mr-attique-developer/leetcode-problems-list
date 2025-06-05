class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        total = 0
        for i in range(2, len(nums)):
            diff1 = nums[i] - nums[i - 1]
            diff2 = nums[i - 1] - nums[i - 2]
            if diff1 == diff2:
                count  += 1
            else:
                total += count * (count + 1) // 2
                count = 0
        return total + count * (count + 1) // 2
            