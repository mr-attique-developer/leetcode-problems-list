class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(map(str,digits)))
        integer +=1
        return [int(i) for i in str(integer)]
    