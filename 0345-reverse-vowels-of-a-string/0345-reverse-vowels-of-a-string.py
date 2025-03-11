class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        l = 0
        r = len(s)- 1
        arr = list(s)
        while l < r:
            if arr[l] not in vowels:
                l += 1
            elif arr[r] not in vowels:
                r -= 1
            else:
                arr[l],arr[r] = arr[r],arr[l]
                l +=1
                r -= 1
        res = "".join(arr)
        return res

        # res = ""
        # vowels = "aeiouAEIOU"
        # stack = []
        # for i in s:
        #     if i in vowels:
        #         stack.append(i)
        # for i in s:
        #     if i in vowels:
        #         res += stack.pop()
        #     else:
        #         res += i
        # return res