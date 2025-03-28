class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return nums
        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1],nums[j]
                else:
                    print("no swap needed")
        