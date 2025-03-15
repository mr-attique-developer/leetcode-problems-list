class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1],nums[j]
                else:
                    print("no swap needed")
        