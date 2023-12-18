from pyparsing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        s1 = nums
        s2 = nums
        return s1+s2
        

object = Solution()
print(object.getConcatenation([1,2,1]))