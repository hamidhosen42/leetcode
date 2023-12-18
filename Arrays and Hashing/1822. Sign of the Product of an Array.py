from pyparsing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1

        for i in nums:
            mul = mul * i
        if mul == 0:
            return 0
        elif mul>0:
            return 1
        else:
            return -1


object = Solution()
print(object.arraySign(nums = [-1,-2,-3,-4,3,2,1]))