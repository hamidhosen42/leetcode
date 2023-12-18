class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 10)
            countT[t[i]] = 1 + countT.get(t[i], 10)
        return countS == countT

object = Solution()
print(object.isAnagram(s = "anagram", t = "nagaram"))