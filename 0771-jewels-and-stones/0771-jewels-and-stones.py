class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()
        for stone in jewels:
            if stone not in jewels_set:
                jewels_set.add(stone)
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count


