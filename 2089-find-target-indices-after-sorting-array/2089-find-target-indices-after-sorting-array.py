class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = 0
        equal = 0
        for i in nums:
            if i < target:
                l += 1
            elif i == target:
                equal += 1
        return list(range(l, l + equal))