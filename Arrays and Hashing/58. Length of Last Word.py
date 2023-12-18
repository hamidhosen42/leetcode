class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list = s.split()
        ln = len(list)

        loflw = len(list[ln-1])
        return loflw
        

object = Solution()
print(object.lengthOfLastWord( s = "Hello World"))