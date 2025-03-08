class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count , pre = 0,0
        for i in flowerbed:
            if i == 1:
                if pre == 1:
                    count -= 1
                pre = 1
            else:
                if pre == 1:
                    pre = 0
                else:
                    count += 1
                    pre = 1
        return count>=n
