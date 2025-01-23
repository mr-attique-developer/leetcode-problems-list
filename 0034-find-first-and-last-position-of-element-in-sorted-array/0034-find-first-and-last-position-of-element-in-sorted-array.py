class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums,target, True)
        right = self.binSearch(nums,target, False)
        return left, right

    def binSearch (self, nums, target, leftBias):
        idx = -1
        left, right = 0 , len(nums)-1
        while left<= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid +1
            else: 
                idx = mid
                if leftBias == True:
                    right = mid -1
                else:
                    left = mid + 1
        return idx
                    
