class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergeList = []
        i= 0
        j = 0
        while i < len(word1) and j < len(word2):
            mergeList.append(word1[i])
            mergeList.append(word2[j])
            i += 1
            j += 1
        
        mergeList.append(word1[i:])
        mergeList.append(word2[j:])
        return "".join(mergeList)
      