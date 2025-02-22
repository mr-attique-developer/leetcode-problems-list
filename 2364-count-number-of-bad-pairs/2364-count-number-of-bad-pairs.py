class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        good_count = 0
        total_paris = (n * (n-1))//2
        for i ,num in enumerate(nums):
            key = num - i
            good_count += dic.get(key,0)
            dic[key] = dic.get(key,0)+1
        return total_paris - good_count