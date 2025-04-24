class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = r 
        while l <= r:
            hours = 0 
            k_mid = (l + r ) // 2
            for p in piles: 
                hours += math.ceil(p / k_mid)
            if hours <= h:
                res = min(res, k_mid)
                r = k_mid - 1
            else:
                l = k_mid + 1
        return res