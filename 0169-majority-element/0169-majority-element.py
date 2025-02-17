class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        temp = len(nums)//2
        return nums[temp]
        # dic = {}
        # for i in nums:
        #     dic[i] = dic.get(i,0) + 1
        #     if dic[i] > len(nums)//2:
        #         return i
